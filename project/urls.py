from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from main.api import viewsets as viewsets

route = routers.DefaultRouter()
route.register(r'produtos',viewsets.ProdutoViewset,basename='produtos')
route.register(r'produtores',viewsets.ProdutorViewset,basename='produtores')
route.register(r'avaliacoes',viewsets.AvaliacaoViewset,basename='avaliacoes')
route.register(r'categorias',viewsets.CategoriaViewset,basename='categorias')
route.register(r'cliques',viewsets.QtdCliquesViewset,basename='qtdcliques')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    