from .views import *
from django.urls import path, include
from rest_framework import routers
router  = routers.DefaultRouter()
# router.register(r'createSale', VentaLocalViewSet)


urlpatterns = [
     path('createOffer/', OfertaView.as_view()),
     path('createSale/', VentaLocalCreateView.as_view()),
     path('uploadImage/', ImagenVentaLocalView.as_view()),
     path("seeAll/",SeeAllOfferView.as_view()),
     path("retrieveImages/", RetrieveImagesView.as_view()),

    # path("seeAllOfferPostulacionUser/",SeeAllOfertaWithPostulacionTransporteView.as_view()),
    # path('', include(router.urls)),
    #path('createSale/', VentaLocalViewSet.as_view()),

]