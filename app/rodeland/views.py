"""
"""

from django.shortcuts import render, redirect


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

def wandel_fiets(request):
    return render(request, 'wandel_fiets.html')

def infomoment(request):
    return render(request, 'infomoment.html')

def poelenfeest(request):
    return render(request, 'poelenfeest.html')


## redirects

def rodelandbrood(request):
    return redirect('https://sites.google.com/view/rodelandbrood')


def wetenschap_op_wieltjes(request):
    return redirect('https://sites.google.com/view/wetenschap-op-wieltjes')
