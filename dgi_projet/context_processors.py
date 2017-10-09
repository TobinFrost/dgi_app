from dgi.models import CategoriePublication,Information,TypeInformation

def get_categorie_publication(request):
    categories = CategoriePublication.objects.all()
    typeInfo = TypeInformation.objects.all()

    return {'categories_publication':categories,'type_information':typeInfo}



def get_information(request):
    informations = Information.objects.all().order_by("-date")
    info_a_chaud = Information.objects.order_by("-date")[:4]
    info_populaire = Information.objects.order_by("-vue")[:4]
    emplois_du_temps = Information.objects.filter(type__libelle__exact="Emplois du Temps")
    return {'informations': informations,'info_a_chaud':info_a_chaud,'info_populaire':info_populaire,'emplois':emplois_du_temps}