from django.http import HttpResponse


def index(request):
    return HttpResponse("Cette Page ne fait pas parti du projet.Veuillez ajouter '/users' sur l'url")