from django.shortcuts import render
from dgi.models import Configuration
# Create your views here.
def index(request):
    conf = Configuration.objects.first()
    mot = conf.mot_du_chef
    miss = conf.mission_departement
    sign = conf.chef_de_departement.compte
    photo_chef = conf.photo_du_chef
    chef = conf.chef_de_departement
    return render(request,'dgi/reindex.html',locals())

def reindex(request):
    conf = Configuration.objects.first()
    mot = conf.mot_du_chef
    miss = conf.mission_departement
    sign = conf.chef_de_departement.compte
    photo_chef = conf.photo_du_chef
    chef = conf.chef_de_departement
    return render(request, 'dgi/reindex.html', locals())