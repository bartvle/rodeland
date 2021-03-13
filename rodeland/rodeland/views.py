"""
"""

from django.shortcuts import render

from actions.models import Realisations


def start(request):
    return render(request, 'start.html')

def wat(request):
    return render(request, 'wat.html')

def wie(request):
    return render(request, 'wie.html')

def acties(request):
    return render(request, 'acties.html')

def contact(request):
    return render(request, 'contact.html')
