# from Crypto import crypto
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import urls
from .models import Reciever, Product
from .forms import RecieverForm
from django.urls import reverse

import hashlib
import json

apiSecret = "NzE1ZGQzZjY2Zjg4YjMyMmMzM2EzOTI1YWFkNGZkMjkwNTNjZWM4ZmM0MDk4ZWU1ZDM"
apiKey = "835b0b13-8861-40dd-9c0b-1bb574265d96"

# request = {
# "toCurrency": "USDT-ERC20",
# "toWallet": "0x0EC964fd9995BfC104937b88b12949d64C20D419",
# "toAmount": "100"
# 'contractCall': {
#     'method': 'methodName',
#     'args': {
#         'arg1': 'arg1',
#         'arg2': 123,
#     },
# },
# }


def convert_to_string(rec):
    def flatten(d, parent_key="", sep=":"):
        items = []
        for key, value in d.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            if isinstance(value, dict):
                items.extend(flatten(value, new_key, sep=sep))
            else:
                items.append(f"{new_key}:{value}")
        return items

    items = flatten(rec)
    items.sort()
    items = "".join(items)
    return items


def generate_sign(rec, secret):
    for_sign = convert_to_string(rec)
    data_to_sign = "".join(for_sign)
    print(data_to_sign)

    hmac = hashlib.new("sha256", secret.encode("utf-8"))
    hmac.update(data_to_sign.encode("utf-8"))
    return hmac.hexdigest()


# signature = generate_sign(request, apiSecret)
# items = convert_to_string(request)


def index_view(request, reciever_id):
    reciever = Reciever.objects.get(id=reciever_id)
    items = reciever.items
    signature = reciever.signature
    return render(
        request,
        "index.html",
        {"signature": signature, "items": items, "apiKey": apiKey},
    )


def account_view(request):
    return render(request, "account.html", {"RecieverForm": RecieverForm})


def registration(request):
    if request.method == "POST":
        form = RecieverForm(request.POST)

        if form.is_valid():

            wallet = form.cleaned_data["wallet"]
            currency = form.cleaned_data["currency"]  # change value!
            amount = form.cleaned_data["amount"]
            description = form.cleaned_data["description"]
            name = form.cleaned_data["name"]
            product = form.cleaned_data["product"]
            request = {"toCurrency": currency, "toWallet": wallet, "toAmount": amount}
            signature = generate_sign(request, apiSecret)
            items = convert_to_string(request)
            reciever = Reciever(
                wallet=wallet,
                name=name,
                items=items,
                signature=signature,
            )
            reciever.save()
            product = Product(
                product_name=product,
                product_description=description,
                currency=currency,
                amount=amount,
                reciever=reciever,
            )
            product.save()
            return HttpResponseRedirect(
                reverse(
                    "index",
                    args=(reciever.id,),
                )
            )


def wallet_view(request):
    return render(request, "offramp.html")


def offramp_view(request):
    return render(request, "offramp_real.html")
