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
    realisations = Realisations.objects.all()
    return render(request, 'acties.html', context={'realsiations': realisations}})

def contact(request):
    return render(request, 'contact.html')
