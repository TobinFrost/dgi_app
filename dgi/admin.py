from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import DGIUser,Agent,Configuration,\
    Departement,Formation,Candidat,Laboratoire,\
    Profession,Serie,Publication,CategoriePublication,\
    Specialite,Information,ServiceEDGI,TypeInformation,Classe

class InformationAdmin(admin.ModelAdmin):
    list_display = ('titre','vue','slug')
    search_fields = ('title',)

admin.site.register(Agent)
admin.site.register(Departement)
admin.site.register(Configuration)
admin.site.register(Formation)
admin.site.register(Candidat)
admin.site.register(Laboratoire)
admin.site.register(Classe)
admin.site.register(Profession)
admin.site.register(Serie)
admin.site.register(Publication)
admin.site.register(CategoriePublication)
admin.site.register(Specialite)
admin.site.register(ServiceEDGI)
admin.site.register(TypeInformation)
admin.site.register(Information,InformationAdmin)



admin.register(DGIUser)

class MyUserAdmin(UserAdmin):
    pass