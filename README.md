<p align="center">
  <img src="./icon/icon.png" alt="Project Icon" width="200" height="200">
</p>

# 💱 Currency Converter API / Conversor de Moedas via API

<p align="center">
  <img src="https://img.shields.io/badge/STATUS-active-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/badge/PROJECT_TYPE-automation-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/TECH_STACK-Python_3.10+-yellow?style=for-the-badge">
  <img src="https://img.shields.io/badge/DEPENDENCIES-requests,_rich,_pytest-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/FEATURES-CLI,_Fallback,_Currency_List-lightgrey?style=for-the-badge">
  <img src="https://img.shields.io/badge/LICENSE-MIT-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/VERSION-1.0.0-red?style=for-the-badge">
  <a href="https://github.com/Joaolbero">
    <img src="https://img.shields.io/badge/AUTHOR-João_Albero-black?style=for-the-badge">
  </a>
  <img src="https://img.shields.io/github/last-commit/Joaolbero/currency-converter-api?style=for-the-badge">
</p>

---

## 📄 Descrição / Description

| 🇧🇷 **Descrição (PT-BR)** | 🇺🇸 **Description (EN)** |
| --- | --- |
| Conversor de moedas via linha de comando (CLI) com fallback automático entre provedores (**ER-API → Frankfurter**). Suporta listagem de moedas, conversão por data, saída estilizada com `rich` ou modo simples (`--plain`) e inclui testes automatizados com Pytest. | Command-line currency converter with automatic provider fallback (**ER-API → Frankfurter**). Supports currency listing, date-based conversion, styled output using `rich`, simple mode (`--plain`), and automated tests using Pytest. |

---

## ✨ Funcionalidades / Features

| 🇧🇷 **Recursos (PT-BR)** | 🇺🇸 **Features (EN)** |
| --- | --- |
| • Conversão de moedas em tempo real<br>• Fallback automático ER-API → Frankfurter<br>• Listagem de moedas disponíveis (`--list`)<br>• CLI estilizada com `rich`<br>• Opção `--plain` para saída simples<br>• Conversão com data específica<br>• Testes automatizados com Pytest | • Real-time currency conversion<br>• Automatic fallback ER-API → Frankfurter<br>• Currency listing (`--list`)<br>• Styled CLI using `rich`<br>• `--plain` option for minimal output<br>• Date-based conversion<br>• Automated tests with Pytest |

---

## 🧩 Instalação / Installation

| 🇧🇷 **Instalação (PT-BR)** | 🇺🇸 **Installation (EN)** |
| --- | --- |
| Instale as dependências globalmente (sem venv). | Install the required dependencies globally (no virtual environment needed). |

### 📥 Passos

    python -m pip install --user requests rich pytest

---

## 🚀 Uso / Usage

### 💰 Conversão padrão / Standard conversion  
    python -m currency_converter.cli --amount 100 --from BRL --to USD

### 🗓️ Conversão com data / Date-based conversion  
    python -m currency_converter.cli --amount 50 --from USD --to JPY --date 2024-12-31

### 🧾 Saída simples / Plain output  
    python -m currency_converter.cli --amount 100 --from EUR --to GBP --plain

### 🌍 Listagem de moedas / Currency list  
    python -m currency_converter.cli --list

### 🔄 Selecionar provedor / Select provider  
    python -m currency_converter.cli --list --provider frankfurter

### 🧪 Testes / Tests  
    python -m pytest -q

---

## 👤 Autor | Author  

Criado por João Albero · 2025  
Created by João Albero · 2025