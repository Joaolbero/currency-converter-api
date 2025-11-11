from __future__ import annotations
import argparse
from rich import print
from .core import ConversionRequest, convert

def main() -> None:
    parser = argparse.ArgumentParser(description="Currency converter (API-backed)")
    parser.add_argument("--amount", type=float, required=True, help="Amount to convert")
    parser.add_argument("--from", dest="from_currency", required=True, help="Source currency code, e.g., BRL")
    parser.add_argument("--to", dest="to_currency", required=True, help="Target currency code, e.g., USD")
    parser.add_argument("--date", type=str, default=None, help="Optional historical date YYYY-MM-DD")
    parser.add_argument("--provider", type=str, default="exchangerate", choices=["exchangerate"], help="FX provider")

    args = parser.parse_args()
    req = ConversionRequest(
        amount=args.amount,
        from_currency=args.from_currency,
        to_currency=args.to_currency,
        date=args.date,
        provider=args.provider,
    )
    res = convert(req)
    print(f"{args.amount:.2f} {args.from_currency.upper()} -> {res['result']:.2f} {args.to_currency.upper()} (rate {res['rate']:.6f} on {res['date']})")

if __name__ == "__main__":
    main()