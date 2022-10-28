from django.shortcuts import render
from django.views import generic
from .models import Producer, Yarn


def get_stash(request):
    yarns = Yarn.objects.all()
    context = {
        'yarns': yarns
    }
    return render(request, 'stash/stash_board.html', context)
