from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Bem vindo(a) ao Portal de Vagas SouJunior!")