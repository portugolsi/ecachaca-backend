from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from main.api import viewsets as viewsets
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


route = routers.DefaultRouter()
route.register(r'produtos',viewsets.ProdutoViewset,basename='produtos')
route.register(r'produtores',viewsets.ProdutorViewset,basename='produtores')
route.register(r'avaliacoes',viewsets.AvaliacaoViewset,basename='avaliacoes')
route.register(r'categorias',viewsets.CategoriaViewset,basename='categorias')
route.register(r'cliques',viewsets.QtdCliquesViewset,basename='qtdcliques'),
route.register(r'usuarios',viewsets.UsuarioViewset,basename='usuarios')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    