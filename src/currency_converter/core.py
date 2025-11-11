from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from .api import RateProvider, OpenERAPIProvider, ConvertResult

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
    raise ValueError(f"Unknown provider: {name}")

def convert(req: ConversionRequest) -> ConvertResult:
    provider = get_provider(req.provider)
    return provider.convert(req.amount, req.from_currency, req.to_currency, req.date)
