"""dgi_projet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views as auth_view
from . import views
from dgi import views as dgiviews
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^agent/register/',dgiviews.register_agent),
    url(r'^login/',auth_view.login,{'template_name': 'dgi/back_log/login.html'},name= "login"),
    #url(r'^login/',dgiviews.mylogin,{'template_name': 'dgi/back_log/login.html'},name= "login"),
    url(r'^candidat/',include("dgi.urls")),
    url(r'^$',views.index,name="index"),
    url(r'^reindex$',views.reindex,name="reindex"),
    #url(r'^actualite$',dgiviews.actualite,name="actualite"),
    url(r'^actualite/$',dgiviews.ActualiteView.as_view(),name="actualite"),
    url(r'^publication/(?P<pk>\d+)$',dgiviews.LirePublication.as_view(),name="detail_publication"),
    url(r'^publications/(?P<id>\d+)$',dgiviews.LirePublicationByCategorie.as_view(),name="publication_by_categorie"),
    url(r'^publications/$',dgiviews.AllPublicationView.as_view(),name="publications"),
    url(r'^agent/(?P<slug>.+)$',dgiviews.AgentProfilView.as_view(),name="profil_agent"),
    url(r'^information/(?P<slug>.+)$',dgiviews.LireInformation.as_view(),name="detail_information"),
    url(r'^laboratoires/$',dgiviews.AllLaboratoireView.as_view(),name="laboratoires"),
    url(r'^informations/(?P<id>\d+)$',dgiviews.LireInformationByCategorie.as_view(),name="information_by_categorie"),
    url(r'^formations/(?P<id>\d+)$',dgiviews.AllFormationByCategorie.as_view(),name="formation_by_categorie"),
    #url(r'^agent/$',dgiviews.profil,name="profil_agent"),
    url(r'^tinymce/$',include('tinymce.urls')),

]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)