from __future__ import annotations
import argparse
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from .core import ConversionRequest, convert

console = Console()

def fmt_amount(v: float) -> str:
    return f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def main() -> None:
    parser = argparse.ArgumentParser(description="Currency converter (API-backed)")
    parser.add_argument("--amount", type=float, required=True, help="Amount to convert")
    parser.add_argument(
        "--from", dest="from_currency", required=True, help="Source currency code, e.g., BRL"
    )
    parser.add_argument(
        "--to", dest="to_currency", required=True, help="Target currency code, e.g., USD"
    )
    parser.add_argument("--date", type=str, default=None, help="Optional historical date YYYY-MM-DD")
    parser.add_argument(
        "--provider", type=str, default="erapi", choices=["erapi"], help="FX provider (no API key)"
    )
    parser.add_argument(
        "--plain", action="store_true",
        help="Disable styled output (prints a single plain line)"
    )

    args = parser.parse_args()
    req = ConversionRequest(
        amount=args.amount,
        from_currency=args.from_currency,
        to_currency=args.to_currency,
        date=args.date,
        provider=args.provider,
    )
    res = convert(req)

    if args.plain:
        print(
            f"{args.amount:.2f} {args.from_currency.upper()} -> "
            f"{res['result']:.2f} {args.to_currency.upper()} "
            f"(rate {res['rate']:.6f} on {res['date']})"
        )
        return

    # Pretty output
    title = Text("Currency Converter", style="bold cyan")
    line1 = Text.assemble(
        ("💱  ", "bold"),
        (fmt_amount(args.amount), "bold white"),
        (f" {args.from_currency.upper()}  →  ", "bright_black"),
        (fmt_amount(res['result']), "bold green"),
        (f" {args.to_currency.upper()}", "bold green"),
    )
    line2 = Text.assemble(
        ("📈  Rate: ", "bright_black"),
        (f"{res['rate']:.6f}", "yellow"),
        ("    "), ("📅  Updated: ", "bright_black"),
        (str(res['date']), "white"),
    )
    body = Text("\n").join([line1, line2])

    console.print(Panel(body, title=title, border_style="cyan", expand=False))


if __name__ == "__main__":
    main()
