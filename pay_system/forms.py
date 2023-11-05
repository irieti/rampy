from django import forms

CRYPTO = (
    (1, "USDT-MATIC"),
    (2, "USDT-ERC20"),
    (3, "USDT-TRC20"),
    (4, "USDT-BEP20"),
    (5, "NEAR"),
    (6, "MATIC"),
    (7, "AVAX"),
    (8, "BTC"),
    (9, "ETH"),
    (10, "FUN-ERC20"),
)


class RecieverForm(forms.Form):
    name = forms.CharField(label="Business name", max_length=100)
    product = forms.CharField(label="Product name", max_length=100)
    description = forms.CharField(label="Product description", max_length=500)
    currency = forms.ChoiceField(label="Choose currency", choices=CRYPTO)
    amount = forms.FloatField(label="Price")
    wallet = forms.CharField(label="Your crypto-wallet address")
