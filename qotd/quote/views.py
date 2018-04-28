from random import randint

from django.shortcuts import render

from quote.models import Quote


def quote(request):
    quotes = Quote.objects.all()
    qotd = quotes[randint(0, len(quotes)-1)]
    # qotd = Quote(content="Legend are made, not born!", author="Yogen Rai", dateCreated=today)
    return render(request, "quote.html", {"quote": qotd})
