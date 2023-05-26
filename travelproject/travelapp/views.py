from django.http import HttpResponse
from django.shortcuts import render

from .models import Place, Team


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    tm = Team.objects.all()
    return render(request, "index.html", {'result': obj,'team':tm})

# def addition(request):
#     x = int(request.GET['n1'])
#     y = int(request.GET['n2'])
#     reslt = x + y
#     return render(request, "result.html", {'result': reslt})

# def about(request):
#     return render(request, "result.html")
#
#
# def contact(request):
#     return HttpResponse("<h1>It's me Contact</h1>")
