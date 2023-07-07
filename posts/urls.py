from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = router.urls
