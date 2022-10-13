from .models import Article
from .serializers import ArticleSerializers

from rest_framework import generics, permissions
from .mixins import StaffEditorPermissions

# Create your views here.

class ArticleListAPIView(generics.ListAPIView, StaffEditorPermissions):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    

class ArticleDetailAPIView(generics.RetrieveAPIView, StaffEditorPermissions):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    lookup_field = 'pk'

class ArticleCreateAPIView(generics.CreateAPIView, StaffEditorPermissions):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    lookup_field = 'pk'

    def perform_create(self, serializer):

        serializer.save()

class ArticleUpdateAPIView(generics.UpdateAPIView, StaffEditorPermissions):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    
    def perform_update(self, serializer):
        return super().perform_update(serializer)

class ArticleDestroyAPIView(generics.DestroyAPIView, StaffEditorPermissions):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)