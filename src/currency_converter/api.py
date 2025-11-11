from __future__ import annotations
import requests
from typing import Optional, TypedDict

class ConvertResult(TypedDict):
    rate: float
    date: str
    result: float

class RateProvider:
    def convert(self, amount: float, from_currency: str, to_currency: str, date: Optional[str] = None) -> ConvertResult:
        raise NotImplementedError

class ExchangerateHostProvider(RateProvider):
    BASE = "https://api.exchangerate.host"

    def convert(self, amount: float, from_currency: str, to_currency: str, date: Optional[str] = None) -> ConvertResult:
        params = {"from": from_currency.upper(), "to": to_currency.upper(), "amount": amount}
        url = f"{self.BASE}/convert"
        if date:
            params["date"] = date
        r = requests.get(url, params=params, timeout=15)
        r.raise_for_status()
        data = r.json()
        if not data.get("success", True):
            raise RuntimeError(f"Conversion error: {data}")
        rate = float(data["info"]["rate"]) if data.get("info") else float(data["result"]) / amount
        date_val = data.get("date")
        return {"rate": rate, "date": date_val, "result": float(data["result"])}

PROVIDERS = {"exchangerate": ExchangerateHostProvider}