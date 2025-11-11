from __future__ import annotations
import requests
from typing import Optional, TypedDict


class ConvertResult(TypedDict):
    rate: float
    date: str
    result: float


class RateProvider:
    def convert(
        self,
        amount: float,
        from_currency: str,
        to_currency: str,
        date: Optional[str] = None,
    ) -> ConvertResult:
        raise NotImplementedError


class OpenERAPIProvider(RateProvider):
    """
    Usa https://open.er-api.com/ (sem API key).
    Suporta BRL, USD, EUR etc. Não tem histórico real; se 'date' vier,
    a conversão vai usar a cotação mais recente assim mesmo.
    """
    BASE = "https://open.er-api.com/v6"

    def convert(
        self,
        amount: float,
        from_currency: str,
        to_currency: str,
        date: Optional[str] = None,
    ) -> ConvertResult:
        base = from_currency.upper()
        target = to_currency.upper()

        url = f"{self.BASE}/latest/{base}"
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        data = r.json()

        if data.get("result") != "success":
            raise RuntimeError(f"Conversion error: {data}")

        rates = data.get("rates", {})
        if target not in rates:
            raise RuntimeError(f"Target currency not available: {target}")

        rate = float(rates[target])
        result = float(amount) * rate
        date_val = data.get("time_last_update_utc", "")

        return {"rate": rate, "date": date_val, "result": result}


# Deixo mapeado caso no futuro você queira voltar pra exchangerate.host com chave
PROVIDERS = {
    "erapi": OpenERAPIProvider,
}