from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth
from django.views.generic import TemplateView

from .forms import MyUserCreationForm,CandidatForm,AgentForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Publication,Agent,Information,Laboratoire,Formation
from django.contrib.auth import authenticate, login
# Create your views here.
def publication(request):
    publi = Publication.objects.first()
    return  render(request,'dgi/publication.html',locals())

def profil(request):

    return render(request,'dgi/front_log/profil.html',locals())


class MyLoginView(TemplateView):
    template_name = "back_log/login.html"


class LireInformation(DetailView):
    model = Information
    context_object_name = 'info'
    template_name = 'dgi/re_information.html'

    def get_object(self):
        pub = super(LireInformation, self).get_object()
        pub.vue += 1
        pub.save()
        return pub



class AllPublicationView(ListView):
    model = Publication
    context_object_name = 'pubs'
    template_name = 'dgi/publications.html'
    def get_queryset(self):
        id_actualite = 2
        #return Publication.objects.filter(categorie__id=id_actualite)
        return Publication.objects.exclude(categorie__id=id_actualite)

class AllLaboratoireView(ListView):
    model = Laboratoire
    context_object_name = 'labos'
    template_name = 'dgi/laboratoires.html'


class AgentProfilView(DetailView):
    context_object_name = "agent"
    template_name = "dgi/front_log/profil.html"
    model = Agent

    def get_context_data(self, **kwargs):
        context = super(AgentProfilView,self).get_context_data(**kwargs)
        agent = context["agent"]
        context["publications"] = Publication.objects.filter(auteurs__compte_id=agent.id)
        return context

class LirePublicationByCategorie(ListView):
    model =  Publication
    context_object_name = 'pubs'
    template_name = 'dgi/publications.html'

    def get_queryset(self):
        return Publication.objects.filter(categorie__id = self.kwargs["id"])


class LireInformationByCategorie(ListView):
    model =  Information
    context_object_name = 'infos'
    template_name = 'dgi/informations.html'

    def get_queryset(self):
        return Information.objects.filter(type__id = self.kwargs["id"])

class AllFormationByCategorie(ListView):
    model =  Formation
    context_object_name = 'formations'
    template_name = 'dgi/formations.html'

    def get_queryset(self):
        return Formation.objects.filter(is_initial = self.kwargs["id"])

class LirePublication(DetailView):
    model = Publication
    context_object_name = 'publi'
    template_name = 'dgi/publication.html'

    def get_object(self):
        pub = super(LirePublication, self).get_object()
        pub.vues += 1
        pub.save()
        return pub


def index(request):

    return render(request,'dgi/index.html',locals())

def actualite(request):
    actualites = Publication.objects.all()
    return render(request,'dgi/actualite.html',locals())


class ActualiteView(ListView):
    model = Information
    context_object_name = "actualites"
    template_name = "dgi/actualite.html"


def logout(request):
    auth.logout(request)
    return render(request, 'dgi/index.html')

def login_back_log(request):

    return render(request, 'dgi/back_log/login.html', locals())


def register_agent(request):
    context = dict()
    ok = False
    if request.method == 'POST':
        uf = MyUserCreationForm(request.POST, prefix='user')
        upf = AgentForm(request.POST or None,request.FILES, prefix='agentprofile')
        context = dict(userform=uf, agentprofileform=upf)
        if uf.is_valid() * upf.is_valid():
            user = uf.save()
            userprofile = upf.save(commit=False)
            userprofile.compte = user
            userprofile.save()
            ok = True
            return HttpResponseRedirect("/agent/register_agent")
    else:
        uf = MyUserCreationForm(prefix='user')
        upf = AgentForm(prefix='agentprofile')
        context = dict(userform=uf,agentprofileform=upf,is_ok=ok)
    return render(request,'dgi/back_log/subscribe.html',context)


def register_candidat(request):
    context = dict()
    if request.method == 'POST':
        uf = MyUserCreationForm(request.POST, prefix='user')
        upf = CandidatForm(request.POST, prefix='userprofile')
        context = dict(userform=uf, userprofileform=upf)
        if uf.is_valid() * upf.is_valid():
            user = uf.save()
            userprofile = upf.save(commit=False)
            userprofile.compte = user
            userprofile.save()
            return HttpResponseRedirect("/candidat/register")
    else:
        uf = MyUserCreationForm(prefix='user')
        upf = CandidatForm(prefix='userprofile')
        context = dict(userform=uf,userprofileform=upf)
    return render(request, 'dgi/front_log/subscribe.html', context)