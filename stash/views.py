from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib import admin
from .models import Yarn, Project
from .forms import AddYarnForm, AddProjectForm


def home(request):
    return render(request, 'stash/index.html')


def user_page(request):
    return render(request, 'stash/user_page.html')


def get_stash(request):
    yarns = Yarn.objects.filter(user=request.user).order_by('-favorite')
    context = {
        'yarns': yarns
    }
    return render(request, 'stash/stash_board.html', context)


def add_yarn(request):
    if request.POST:
        form = AddYarnForm(request.POST)

        if form.is_valid():
            print("FORM IS VALID")
            form = form.save(commit=False)
            form.user = request.user
            form.save()
        else:
            print("ERROR", form.errors)
        return redirect('get_stash')
    return render(request, 'stash/add_yarn.html', {'form': AddYarnForm})


def edit_yarn(request, yarn_id):
    yarn = get_object_or_404(Yarn, id=yarn_id)
    if request.POST:
        form = AddYarnForm(request.POST, instance=yarn)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
        return redirect('get_stash')
    form = AddYarnForm(instance=yarn)
    context = {
        'form': form
    }
    return render(request, 'stash/edit_yarn.html', context, )


def delete_yarn(request, yarn_id):
    yarn = get_object_or_404(Yarn, id=yarn_id)
    yarn.delete()
    return redirect('get_stash')


def get_projects(request):
    projects = Project.objects.filter(user=request.user).order_by('finished')
    context = {
        'projects': projects
    }
    paginate_by = 12
    return render(request, 'stash/projects_board.html', context)


def add_project(request):
    if request.POST:
        form = AddProjectForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
        return redirect('get_projects')
    return render(request, 'stash/add_project.html', {'form': AddProjectForm})


def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.POST:
        form = AddProjectForm(request.POST, instance=project)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
        return redirect('get_projects')
    form = AddProjectForm(instance=project)
    context = {
        'form': form
    }
    return render(request, 'stash/edit_project.html', context, )


def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return redirect('get_projects')