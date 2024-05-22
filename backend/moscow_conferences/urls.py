from moscow_conferences_api.views import ConferencesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/v1/conferences', ConferencesViewSet, basename='api/v1/conferences')
urlpatterns = router.urls
