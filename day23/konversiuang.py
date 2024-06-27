def convert_currency(amount, rate):
    return amount * rate

usd_to_eur_rate = 0.85
usd_amount = 100
eur_amount = convert_currency(usd_amount, usd_to_eur_rate)

print(f"${usd_amount} USD is equal to €{eur_amount:.2f} EUR")
