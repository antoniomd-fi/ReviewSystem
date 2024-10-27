from rest_framework.routers import DefaultRouter
from .views import BusinessViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'businesses', BusinessViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = router.urls
