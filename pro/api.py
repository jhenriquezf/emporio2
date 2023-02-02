from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewsSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer