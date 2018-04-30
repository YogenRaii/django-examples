from random import randint

from django.shortcuts import render

from quote.models import Quote


def quote(request):
    quotes = Quote.objects.all()
    qotd = quotes[randint(0, len(quotes)-1)]
    return render(request, "quote.html", {"quote": qotd})
