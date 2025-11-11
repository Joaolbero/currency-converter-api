from currency_converter.core import ConversionRequest, convert

def test_smoke_request_build():
    req = ConversionRequest(amount=1.0, from_currency="USD", to_currency="BRL")
    assert req.amount == 1.0
    assert req.from_currency == "USD"
    assert req.to_currency == "BRL"