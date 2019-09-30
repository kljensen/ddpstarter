from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    context_data = {
        "session": request.session
    }
    return render(request, 'index.html', context_data)
