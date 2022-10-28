from django.shortcuts import render
from django.views import generic
from .models import Producer


def testing(request):
    return render(request, 'stash/stash_board.html')
