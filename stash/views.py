from django.shortcuts import render
from django.views import generic
from .models import Producer, Yarn, Material, Color, Weight, Amount


def get_home(request):
    return render(request, 'stash/index.html')


def get_stash(request):
    yarns = Yarn.objects.all()
    context = {
        'yarns': yarns
    }
    paginate_by = 12
    return render(request, 'stash/stash_board.html', context)
