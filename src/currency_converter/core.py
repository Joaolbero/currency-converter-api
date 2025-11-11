from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from .api import RateProvider, ExchangerateHostProvider, ConvertResult

@dataclass
class ConversionRequest:
    amount: float
    from_currency: str
    to_currency: str
    date: Optional[str] = None
    provider: str = "exchangerate"

def get_provider(name: str) -> RateProvider:
    if name == "exchangerate":
        return ExchangerateHostProvider()
    raise ValueError(f"Unknown provider: {name}")

def convert(req: ConversionRequest) -> ConvertResult:
    provider = get_provider(req.provider)
    return provider.convert(req.amount, req.from_currency, req.to_currency, req.date)