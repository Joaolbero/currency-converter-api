# 💱 Conversor de Moedas com API / Currency Converter (API)

> Projeto em Python com **CLI estilizada**, **listagem de moedas** e **fallback automático de provedores**.  
> Sem ambiente virtual (*No venv*).  
> API pública e gratuita: [ER-API](https://open.er-api.com/) + [Frankfurter](https://www.frankfurter.app/).

---

## 🧠 Funcionalidades / Features
✅ Conversão de moedas com cotação atual  
✅ Fallback automático ER-API → Frankfurter  
✅ Listagem de moedas disponíveis (`--list`)  
✅ CLI com Rich (painéis e cores)  
✅ Opção `--plain` para saída simples  
✅ Testes automatizados com Pytest  

---

## ⚙️ Requisitos / Requirements
Python 3.10+  
Bibliotecas:
```bash
python -m pip install --user requests rich pytest

# Conversão padrão
python -m currency_converter.cli --amount 100 --from BRL --to USD

# Data específica
python -m currency_converter.cli --amount 50 --from USD --to JPY --date 2024-12-31

# Saída sem Rich
python -m currency_converter.cli --amount 100 --from EUR --to GBP --plain

# Listar moedas disponíveis
python -m currency_converter.cli --list

# Provedor Alternativo
python -m currency_converter.cli --list --provider frankfurter

# Testes
python -m pytest -q
