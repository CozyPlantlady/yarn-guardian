from django.shortcuts import render, redirect
from django.views import generic
from .models import Producer, Yarn, Material, Color, Weight, Amount
from .forms import UploadForm


def home(request):
    return render(request, 'stash/index.html')


def get_stash(request):
    yarns = Yarn.objects.all()
    context = {
        'yarns': yarns
    }
    paginate_by = 12
    return render(request, 'stash/stash_board.html', context)


def add_yarn(request):
    if request.POST:
        form = UploadForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('get_stash')
    return render(request, 'stash/add_yarn.html', {'form': UploadForm})


# def upload(request):
#    form = UploadForm(request.POST)
#    return render(request, 'stash/add_yarn.html', {'form': form})
