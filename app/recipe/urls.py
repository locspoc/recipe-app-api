from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views


router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)

app_name = 'recipe'

urlpatterns = [
<<<<<<< HEAD
    path('/', include(router.urls))
=======
    path('', include(router.urls))
>>>>>>> a1f688f3ab6cf1334a9f292ded1f54c8b724c840
]
