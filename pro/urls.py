from rest_framework import routers
from .api import ProjectViewsSet

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewsSet, 'projects')

urlpatterns = router.urls