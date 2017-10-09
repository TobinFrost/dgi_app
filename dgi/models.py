#coding=utf-8
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from tinymce.models import HTMLField
from django.utils.translation import ugettext_lazy as _

class DGIUser(AbstractUser):

    class Meta:
        unique_together = ('email',)
        verbose_name = "Utilisateur"



    def __unicode__(self):
        return u"[{0}]".format(self.email)

class Agent(models.Model):
    compte = models.OneToOneField(DGIUser,on_delete=models.CASCADE)
    matricule = models.CharField(max_length=9)
    telephone = models.CharField(max_length=20,null=True,default="")
    profession = models.ForeignKey('Profession',null=True)
    is_laborantin = models.BooleanField(default=False)
    curriculum = HTMLField(null=True,default="")
    cv = HTMLField(null=True,default="")
    parcours_pro = HTMLField(null=True,verbose_name="Parcours Professionnel",default="This is a text")
    parcours_aca = HTMLField(null=True,verbose_name="Parcours Académique",default="This is a text")
    enseignements = HTMLField(null=True,verbose_name="Enseignements",default="This is a text")
    recherches = HTMLField(null=True,verbose_name="Recherches",default="This is a text")
    encadrements = HTMLField(null=True,verbose_name="Encadrements",default="This is a text")
    photo = models.ImageField(upload_to="photos/",null=True,default="")

    slug = models.SlugField()




    def __unicode__(self):
        return u"[{0}] {1}".format(self.compte.first_name, self.compte.last_name)


################## FIN CLASSE AGENT ###############################

class Profession(models.Model):
    libelle = models.CharField(max_length=100)
    specialite = models.ForeignKey('Specialite')

    def __unicode__(self):
        return u"{0}".format(self.libelle)

class Specialite(models.Model):
    libelle = models.CharField(max_length=100)
    def __unicode__(self):
        return u"{0}".format(self.libelle)



class Laboratoire(models.Model):
    libelle = models.CharField(max_length=150)
    code = models.CharField(max_length=50,null=True)
    description = models.TextField(null=True)
    chef = models.ForeignKey(Agent)
    def __unicode__(self):
        return u"[{0}]".format(self.libelle)


class Configuration(models.Model):
    mission_departement = models.TextField(null=True)
    mot_du_chef = models.TextField(null=True)
    chef_de_departement = models.ForeignKey(Agent)
    photo_du_chef = models.ImageField(upload_to="photos/", null=True, default="")


class TypeInformation(models.Model):
    libelle = models.CharField(max_length=50)

    def __unicode__(self):
        return u"{0}".format(self.libelle)


class CategoriePublication(models.Model):
    libelle = models.CharField(max_length=50)
    def __unicode__(self):
            return u"[{0}]".format(self.libelle)

class Information(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField(default="")
    image = models.ImageField(upload_to="information_image/",verbose_name="Image de Couverture")
    slug = models.SlugField()
    type = models.ForeignKey(TypeInformation,null=True,verbose_name="Type Information")
    date = models.DateField(verbose_name="Date de Publication",default=timezone.now())
    fichier = models.FileField(upload_to="information_fichier/%Y/%m/%d",verbose_name="Fichier Associé",null=True)
    vue = models.IntegerField(default=0,verbose_name="Nombre de Consultations")
    def __unicode__(self):
            return u"{0}".format(self.titre)


class Publication(models.Model):
    titre = models.CharField(max_length=150)
    auteurs = models.ManyToManyField(Agent)
    pages = models.CharField(max_length=50)
    categorie = models.ManyToManyField(CategoriePublication)
    vues = models.IntegerField(default=0)
    annee = models.IntegerField(null=True)
    lien = models.URLField(verbose_name="Lien vers Article", default="")
    reference = models.URLField(null=True,verbose_name="Lien vers Référence")
    libelle_reference = models.CharField(max_length=50, verbose_name="Libelle Référence", default="")
    detail_reference = models.CharField(max_length=50, verbose_name="Détail Référence", default="")

    date_post = models.DateField(default=timezone.now())


    #slug = models.SlugField()

    def __unicode__(self):
            return u"[{0}]".format(self.titre)

class Departement(models.Model):
    libelle = models.CharField(max_length=50)
    def __unicode__(self):
        return u"{0}".format(self.libelle)

class Serie(models.Model):
    libelle = models.CharField(max_length=2)
    def __unicode__(self):
        return u"{0}".format(self.libelle)

class Formation(models.Model):
    libelle = models.CharField(max_length=50)
    code = models.CharField(max_length=8)
    departement = models.ForeignKey(Departement)
    serie = models.ManyToManyField(Serie)
    is_initial = models.BooleanField()
    def __unicode__(self):
        return u"{0}".format(self.libelle)

class Classe(models.Model):
    libelle = models.CharField(max_length=50)
    code = models.CharField(max_length=8)
    formation = models.ForeignKey(Formation)
    def __unicode__(self):
        return u"{0}".format(self.libelle)

class Candidat(models.Model):
    compte = models.OneToOneField(DGIUser, on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)
    formation_asked = models.ForeignKey(Formation, null=True)
    telephone = models.CharField(max_length=20, null=False)

class ServiceEDGI(models.Model):
    class Meta:
        verbose_name = "Service E-DGI"
    libelle = models.CharField(max_length=50)
    description = models.TextField()
    liens = models.URLField(verbose_name="Lien vers le service")
    def __unicode__(self):
        return u"{0}".format(self.libelle)

