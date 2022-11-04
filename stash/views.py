from django.shortcuts import render, redirect
from django.views import generic
from .models import Producer, Yarn, Material, Color, Weight, Amount, User
from .forms import AddYarnForm


def home(request):
    return render(request, 'stash/index.html')


def get_stash(request):
    yarns = Yarn.objects.filter(user=request.user)
    context = {
        'yarns': yarns
    }
    paginate_by = 12
    return render(request, 'stash/stash_board.html', context)


def add_yarn(request):
    if request.POST:
        form = AddYarnForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
        return redirect('get_stash')
    return render(request, 'stash/add_yarn.html', {'form': AddYarnForm})
