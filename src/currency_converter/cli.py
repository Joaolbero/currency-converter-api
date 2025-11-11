from __future__ import annotations
import argparse
from math import ceil
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from .core import ConversionRequest, convert, list_currencies

console = Console()

def fmt_amount(v: float) -> str:
    return f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def show_list(provider: str) -> None:
    data = list_currencies(provider)
    codes = sorted(data.keys())
    table = Table(title=f"Moedas suportadas ({provider})", show_lines=False)
    table.add_column("Código", style="cyan", no_wrap=True)
    table.add_column("Nome", style="white")
    for c in codes:
        table.add_row(c, data.get(c, c))
    console.print(table)

def main() -> None:
    parser = argparse.ArgumentParser(description="Currency converter (API-backed, with fallback)")
    parser.add_argument("--amount", type=float, help="Amount to convert")
    parser.add_argument("--from", dest="from_currency", help="Source currency code, e.g., BRL")
    parser.add_argument("--to", dest="to_currency", help="Target currency code, e.g., USD")
    parser.add_argument("--date", type=str, default=None, help="Optional historical date YYYY-MM-DD")
    parser.add_argument("--provider", type=str, default="erapi", choices=["erapi", "frankfurter"], help="Preferred provider (no API key)")
    parser.add_argument("--plain", action="store_true", help="Plain output (single line)")
    parser.add_argument("--list", action="store_true", help="List supported currencies and exit")

    args = parser.parse_args()

    if args.list:
        show_list(args.provider)
        return

    # validação simples
    if args.amount is None or not args.from_currency or not args.to_currency:
        parser.error("--amount, --from e --to são obrigatórios (ou use --list)")

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
            f"(rate {res['rate']:.6f} on {res['date']} via {res['provider']})"
        )
        return

    title = Text("Currency Converter", style="bold cyan")
    line1 = Text.assemble(
        ("💱  ", "bold"),
        (fmt_amount(args.amount), "bold white"),
        (f" {args.from_currency.upper()}  →  ", "bright_black"),
        (fmt_amount(res['result']), "bold green"),
        (f" {args.to_currency.upper()}", "bold green"),
    )
    line2 = Text.assemble(
        ("📈  Rate: ", "bright_black"), (f"{res['rate']:.6f}", "yellow"),
        ("    "), ("📅  Updated: ", "bright_black"), (str(res['date']), "white"),
        ("    "), ("🛰  Provider: ", "bright_black"), (res.get("provider","?"), "magenta"),
    )
    body = Text("\n").join([line1, line2])
    console.print(Panel(body, title=title, border_style="cyan", expand=False))


if __name__ == "__main__":
    main()