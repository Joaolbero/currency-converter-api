from __future__ import annotations
import requests
from typing import Optional, TypedDict, Dict


class ConvertResult(TypedDict):
    rate: float
    date: str
    result: float
    provider: str  # quem respondeu


class RateProvider:
    name: str = "base"

    def convert(
        self,
        amount: float,
        from_currency: str,
        to_currency: str,
        date: Optional[str] = None,
    ) -> ConvertResult:
        raise NotImplementedError

    def list_currencies(self) -> Dict[str, str]:
        """Retorna { 'USD': 'US Dollar', ... } quando disponível.
        Se o provedor não tiver endpoint de nomes, retorna só {'USD': 'USD', ... }."""
        raise NotImplementedError


# -------------------------------
# Provider 1: open.er-api.com (sem API key)
# -------------------------------
class OpenERAPIProvider(RateProvider):
    name = "erapi"
    BASE = "https://open.er-api.com/v6"

    def _latest(self, base: str):
        url = f"{self.BASE}/latest/{base}"
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        data = r.json()
        if data.get("result") != "success":
            raise RuntimeError(f"ER-API error: {data}")
        return data

    def convert(
        self, amount: float, from_currency: str, to_currency: str, date: Optional[str] = None
    ) -> ConvertResult:
        base = from_currency.upper()
        target = to_currency.upper()
        data = self._latest(base)
        rates = data.get("rates", {})
        if target not in rates:
            raise RuntimeError(f"ER-API: target not available: {target}")
        rate = float(rates[target])
        result = float(amount) * rate
        date_val = data.get("time_last_update_utc", "")
        return {"rate": rate, "date": date_val, "result": result, "provider": self.name}

    def list_currencies(self) -> Dict[str, str]:
        # ER-API não tem endpoint de nomes; devolvemos as keys como nome = código
        data = self._latest("USD")  # qualquer base serve só para descobrir keys
        return {code: code for code in data.get("rates", {}).keys()}


# -------------------------------
# Provider 2: frankfurter.app (sem API key)
# -------------------------------
class FrankfurterProvider(RateProvider):
    name = "frankfurter"
    BASE = "https://api.frankfurter.app"

    def convert(
        self, amount: float, from_currency: str, to_currency: str, date: Optional[str] = None
    ) -> ConvertResult:
        base = from_currency.upper()
        target = to_currency.upper()
        # Frankfurter permite histórico via /YYYY-MM-DD
        path = f"/{date}" if date else "/latest"
        url = f"{self.BASE}{path}"
        r = requests.get(url, params={"from": base, "to": target}, timeout=15)
        r.raise_for_status()
        data = r.json()
        rates = data.get("rates", {})
        if target not in rates:
            raise RuntimeError(f"Frankfurter: target not available: {target}")
        rate = float(rates[target])
        result = float(amount) * rate
        date_val = data.get("date", "")
        return {"rate": rate, "date": date_val, "result": result, "provider": self.name}

    def list_currencies(self) -> Dict[str, str]:
        url = f"{self.BASE}/currencies"
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        data = r.json()  # { "USD": "US Dollar", ... }
        return {k: str(v) for k, v in data.items()}


PROVIDERS = {
    "erapi": OpenERAPIProvider,
    "frankfurter": FrankfurterProvider,
}