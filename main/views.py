from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.contenttypes.models import ContentType
from rest_framework import status
from rest_framework.renderers import JSONRenderer

import main.models
import main.serializers


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'articles': reverse('article-list', request=request, format=format),
        'news': reverse('news-list', request=request, format=format),
        'article-comments': reverse('article-comment-list', request=request, format=format),
        'news-comments': reverse('news-comment-list', request=request, format=format),
        'article-votes': reverse('article-vote-list', request=request, format=format),
        'news-votes': reverse('news-vote-list', request=request, format=format),
        'comment-votes': reverse('comment-vote-list', request=request, format=format),
    })


class CommentVoteCountView(APIView):
    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        try:
            comment = int(self.request.query_params.get('comment', None))
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        plus_count = main.models.Vote.objects.filter(
            content_type=ContentType.objects.get(app_label='main', model='comment'),
            object_id=comment,
            vote='plus',
        ).count()
        minus_count = main.models.Vote.objects.filter(
            content_type=ContentType.objects.get(app_label='main', model='comment'),
            object_id=comment,
            vote='minus',
        ).count()
        content = {
            'plus_count': plus_count,
            'minus_count': minus_count,
            'vote_count': plus_count + minus_count,
        }
        return Response(content)


class ArticleVoteCountView(APIView):
    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        try:
            article = int(self.request.query_params.get('article', None))
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        plus_count = main.models.Vote.objects.filter(
            content_type=ContentType.objects.get(app_label='main', model='article'),
            object_id=article,
            vote='plus',
        ).count()
        minus_count = main.models.Vote.objects.filter(
            content_type=ContentType.objects.get(app_label='main', model='article'),
            object_id=article,
            vote='minus',
        ).count()
        content = {
            'plus_count': plus_count,
            'minus_count': minus_count,
            'vote_count': plus_count + minus_count,
        }
        return Response(content)


class NewsVoteCountView(APIView):
    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        try:
            news = int(self.request.query_params.get('news', None))
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        plus_count = main.models.Vote.objects.filter(
            content_type=ContentType.objects.get(app_label='main', model='news'),
            object_id=news,
            vote='plus',
        ).count()
        minus_count = main.models.Vote.objects.filter(
            content_type=ContentType.objects.get(app_label='main', model='news'),
            object_id=news,
            vote='minus',
        ).count()
        content = {
            'plus_count': plus_count,
            'minus_count': minus_count,
            'vote_count': plus_count + minus_count,
        }
        return Response(content)


class ArticleList(generics.ListCreateAPIView):
    queryset = main.models.Article.objects.all()
    serializer_class = main.serializers.ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = main.models.Article.objects.all()
    serializer_class = main.serializers.ArticleSerializer


class NewsList(generics.ListCreateAPIView):
    queryset = main.models.News.objects.all()
    serializer_class = main.serializers.NewsSerializer


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = main.models.News.objects.all()
    serializer_class = main.serializers.NewsSerializer


class ArticleCommentList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = main.models.Comment.objects.filter(
            content_type=ContentType.objects.get(app_label='main', model='article')
        )
        article_id = self.request.query_params.get('article', None)
        if article_id:
            queryset = queryset.filter(object_id=article_id)
        return queryset

    serializer_class = main.serializers.ArticleCommentSerializer


class ArticleCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = main.models.Comment.objects.filter(
        content_type=ContentType.objects.get(app_label='main', model='article')
    )
    serializer_class = main.serializers.ArticleCommentSerializer


class NewsCommentList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = main.models.Comment.objects.filter(
            content_type=ContentType.objects.get(app_label='main', model='news')
        )
        news_id = self.request.query_params.get('news', None)
        if news_id:
            queryset = queryset.filter(object_id=news_id)
        return queryset
    serializer_class = main.serializers.NewsCommentSerializer


class NewsCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = main.models.Comment.objects.filter(
        content_type=ContentType.objects.get(app_label='main', model='news')
    )
    serializer_class = main.serializers.NewsCommentSerializer


class ArticleVoteList(generics.ListCreateAPIView):
    queryset = main.models.Vote.objects.filter(
        content_type=ContentType.objects.get(app_label='main', model='article')
    )
    serializer_class = main.serializers.ArticleVoteSerializer


class ArticleVoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = main.models.Vote.objects.filter(
        content_type=ContentType.objects.get(app_label='main', model='article')
    )
    serializer_class = main.serializers.ArticleVoteSerializer


class NewsVoteList(generics.ListCreateAPIView):
    queryset = main.models.Vote.objects.filter(
        content_type=ContentType.objects.get(app_label='main', model='news')
    )
    serializer_class = main.serializers.NewsVoteSerializer


class NewsVoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = main.models.Vote.objects.filter(
        content_type=ContentType.objects.get(app_label='main', model='news')
    )
    serializer_class = main.serializers.NewsVoteSerializer


class CommentVoteList(generics.ListCreateAPIView):
    queryset = main.models.Vote.objects.filter(
        content_type=ContentType.objects.get(app_label='main', model='comment')
    )
    serializer_class = main.serializers.CommentVoteSerializer


class CommentVoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = main.models.Vote.objects.filter(
        content_type=ContentType.objects.get(app_label='main', model='comment')
    )
    serializer_class = main.serializers.CommentVoteSerializer
