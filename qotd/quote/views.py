from datetime import datetime

from django.shortcuts import render
from quote.models import Quote


def quote(request):
    # return HttpResponse("Legend are made, not born!")
    today = datetime.now().date()
    qotd = Quote(content="Legend are made, not born!", author="Yogen Rai", dateCreated=today)
    return render(request, "quote.html", {"quote": qotd})
