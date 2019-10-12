from django.db.models.functions import Lower
from django.http import JsonResponse
from django.shortcuts import render
from rooms.models import Book


def search(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        results = []
        if len(q) > 1:
            results = list(Book.objects.filter(title__istartswith=q).values_list(Lower('title'), flat=True))
        return JsonResponse(results, safe=False)
    else:
        return render(request, "rooms/base.html")
