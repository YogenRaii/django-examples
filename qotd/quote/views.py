from random import randint

from django.shortcuts import render

from quote.forms import LoginForm
from quote.models import Quote


def quote(request):
    quotes = Quote.objects.all()
    qotd = quotes[randint(0, len(quotes) - 1)]
    return render(request, "quote.html", {"quote": qotd})


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data['username']

        return render(request, "dashboard.html", {"username": username})
    else:
        login_form = LoginForm()
        return render(request, "login.html", {"form": login_form})

