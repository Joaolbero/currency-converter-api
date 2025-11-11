from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Dict, List
from .api import RateProvider, OpenERAPIProvider, FrankfurterProvider, ConvertResult


@dataclass
class ConversionRequest:
    amount: float
    from_currency: str
    to_currency: str
    date: Optional[str] = None
    provider: str = "erapi"  # padrão sem API key


def get_provider(name: str) -> RateProvider:
    if name == "erapi":
        return OpenERAPIProvider()
    if name == "frankfurter":
        return FrankfurterProvider()
    raise ValueError(f"Unknown provider: {name}")


def convert(req: ConversionRequest) -> ConvertResult:
    # Fallback: tenta o escolhido → cai pros demais
    order: List[str] = [req.provider] + [p for p in ["erapi", "frankfurter"] if p != req.provider]
    last_err: Optional[Exception] = None
    for name in order:
        try:
            prov = get_provider(name)
            res = prov.convert(req.amount, req.from_currency, req.to_currency, req.date)
            return res
        except Exception as e:
            last_err = e
            continue
    raise RuntimeError(f"All providers failed. Last error: {last_err}")


def list_currencies(provider_name: str = "erapi") -> Dict[str, str]:
    prov = get_provider(provider_name)
    return prov.list_currencies()