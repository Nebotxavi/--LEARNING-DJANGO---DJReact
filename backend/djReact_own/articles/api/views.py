from rest_framework.generics import ListAPIView, RetrieveAPIView

from articles.models import Article
from .serializers import ArticleSerializer


class ArticleListViews(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailsView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
