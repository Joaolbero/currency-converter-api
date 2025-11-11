# 💱 Conversor de Moedas com API / Currency Converter (API)

> Projeto em Python com **CLI estilizada**, **listagem de moedas** e **fallback automático de provedores**.  
> Sem ambiente virtual (*No venv*).  
> API pública e gratuita: [ER-API](https://open.er-api.com/) + [Frankfurter](https://www.frankfurter.app/).

🇺🇸 English Summary

Python project featuring a modern CLI, currency listing, and automatic provider fallback.
No virtual environment required.
Uses free and public APIs: ER-API
and Frankfurter
.

Highlights

Real-time currency conversion

Automatic fallback: ER-API → Frankfurter

--list command to show all supported currencies

Styled CLI using Rich

--plain option for simple text output

Fully tested with Pytest

Example commands
python -m currency_converter.cli --amount 100 --from BRL --to USD
python -m currency_converter.cli --amount 50 --from USD --to JPY --date 2024-12-31
python -m currency_converter.cli --list

---

## 🇧🇷 Funcionalidades / 🇺🇸 Features
✅ Conversão de moedas com cotação atual / Real-time currency conversion  
✅ Fallback automático ER-API → Frankfurter / Automatic fallback between APIs  
✅ Listagem de moedas disponíveis (`--list`) / List all supported currencies  
✅ CLI com Rich (painéis e cores) / Styled CLI with colors  
✅ Opção `--plain` para saída simples / Plain text output  
✅ Testes automatizados com Pytest / Automated testing with Pytest  

---

## ⚙️ Requisitos / Requirements
**Python 3.10+**

📦 Bibliotecas / Dependencies:
```bash
python -m pip install --user requests rich pytest

🚀 Uso / Usage
💰 Conversão padrão / Standard conversion
python -m currency_converter.cli --amount 100 --from BRL --to USD

🗓️ Data específica / Specific date
python -m currency_converter.cli --amount 50 --from USD --to JPY --date 2024-12-31

🧾 Saída sem Rich / Without Rich formatting
python -m currency_converter.cli --amount 100 --from EUR --to GBP --plain

🌍 Listar moedas disponíveis / List available currencies
python -m currency_converter.cli --list

🔄 Provedor alternativo / Alternative provider
python -m currency_converter.cli --list --provider frankfurter

🧪 Testes / Tests
python -m pytest -q

✅ Esperado / Expected: 1 passed in X.XXs

