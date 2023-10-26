from django.shortcuts import render, reverse, HttpResponseRedirect
from .models import Disco, Artista
from django.db import models
from .forms import DiscoForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
def dashboard(request):
    total_discos = Disco.objects.count()
    total_artistas = Artista.objects.count()
    total_copias = Disco.objects.aggregate(total_copias=models.Sum("quantidade"))
    resultado = total_copias["total_copias"]
    context = {
        "total_discos": total_discos,
        "total_artistas": total_artistas,
        "total_copias": resultado,
    }
    return render(request, "disco/dashboard.html", context)


@login_required
def index(request):
    discos = Disco.objects.all()
    artistas = Artista.objects.all()

    nome_disco = request.GET.get("nome_disco")
    if nome_disco:
        discos = discos.filter(nome__icontains=nome_disco)

    artista = request.GET.get("artista")
    if artista and artista != "-1":
        discos = discos.filter(artistas__nome__icontains=artista)

    paginator = Paginator(discos, 10)
    pagina_atual = request.GET.get("p", 1)
    discos = paginator.get_page(pagina_atual)

    context = {"discos": discos, "artistas": artistas}
    return render(request, "disco/discos.html", context)


@login_required
def create_disco(request):
    context = {"acao": "Cadastrar"}
    if request.POST:
        form = DiscoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            context["form"] = form
            return render(request, "disco/form.html", context)
    else:
        context["form"] = DiscoForm()

        return render(request, "disco/form.html", context)


@login_required
def edit_disco(request, pk):
    context = {"acao": "Editar"}
    if request.POST:
        form = DiscoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            context["form"] = form
            return render(request, "disco/form.html", context)
    else:
        disco = Disco.objects.get(pk=pk)
        form = DiscoForm(instance=disco)
        context["form"] = form

        return render(request, "disco/form.html", context)


@login_required
def delete_disco(request, pk):
    disco = Disco.objects.get(pk=pk)
    disco.delete()
    return HttpResponseRedirect(reverse("index"))


def login(request):
    return render(request, "disco/accounts/login.html")
