"""
"""

from django.shortcuts import render


def start(request):
    return render(request, 'start.html')

def wat(request):
    return render(request, 'wat.html')

def wie(request):
    return render(request, 'wie.html')

def acties(request):
    return render(request, 'acties.html')

def pdpo(request):
    return render(request, 'pdpo.html')

def contact(request):
    return render(request, 'contact.html')

def infomoment(request):
    return render(request, 'infomoment.html')

def poelenfeest(request):
    return render(request, 'poelenfeest.html')
