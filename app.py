import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("EXCHANGE_API_KEY")

st.set_page_config(page_title="USD Currency Converter", page_icon="💵")

st.title("💵 USD to Currency Converter")


with open(r"D:\Python Project\abbrivation.json", "r") as f:
    data = json.load(f)

country_codes = {}

for item in data:
    country_codes[item["country"]] = item["currency_code"]

countries = sorted(country_codes.keys())

url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"

response = requests.get(url)
exchange_data = response.json()

usd = st.number_input(
    "Enter Amount in USD",
    min_value=0.0,
    value=1.0,
    step=1.0
)

country = st.selectbox(
    "Select Country",
    countries
)


if st.button("Convert"):

    code = country_codes[country]

    if code in exchange_data["conversion_rates"]:

        converted_amount = usd * exchange_data["conversion_rates"][code]

        st.success(f"💰 {usd:.2f} USD = {converted_amount:.2f} {code}")

    else:
        st.error("Currency not available.")