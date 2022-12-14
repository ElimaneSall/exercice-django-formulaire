from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .form import ProfesseurForm
from .models import Professeur


def index(request):
    base = Professeur.objects.all()
    return render(request, 'index.html', {'base_donnee':base})


def formprof(request):
    form = ProfesseurForm(request.POST)
    if request.method == "POST":
        form = ProfesseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfesseurForm
        return render(request, 'formprof.html', {'form': form})


def formprof2(request):
    if request.method == "GET":
        if request.GET.get("nom") and request.GET.get("prenom") and request.GET.get("email"):
            form = Professeur()
            form.nom = request.GET.get("nom")
            form.prenom = request.GET.get("prenom")
            form.email = request.GET.get("email")
            form.contact = request.GET.get("contact")
            form.date_adhesion = request.GET.get("date_adhesion")
            form.chef_department = request.GET.get("chef_department")
            if request.GET.get("chef_department"):
                form.chef_department = True
            else:
                form.chef_department = False
            form.save()
            return redirect('index')
        else:
            form = ProfesseurForm
            return render(request, 'formprof2.html', {'form': form})

    else:
        form = ProfesseurForm
        return render(request, 'formprof2.html', {'form': form})

