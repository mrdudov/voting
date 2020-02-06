from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from main import views


urlpatterns = [
    path('', views.api_root),


    path('comment/count/', views.CommentVoteCountView.as_view(), name='comment-count'),
    path('article/count/', views.ArticleVoteCountView.as_view(), name='article-count'),
    path('news/count/', views.NewsVoteCountView.as_view(), name='news-count'),

    path('articles/', views.ArticleList.as_view(), name='article-list'),
    path('articles/<int:pk>', views.ArticleDetail.as_view(), name='article-detail'),

    path('news/', views.NewsList.as_view(), name='news-list'),
    path('news/<int:pk>', views.NewsDetail.as_view(), name='news-detail'),

    path('article-comments/', views.ArticleCommentList.as_view(), name='article-comment-list'),
    path('article-comments/<int:pk>', views.ArticleCommentDetail.as_view(), name='article-comment-detail'),

    path('news-comments/', views.NewsCommentList.as_view(), name='news-comment-list'),
    path('news-comments/<int:pk>', views.NewsCommentDetail.as_view(), name='news-comment-detail'),

    path('article-votes/', views.ArticleVoteList.as_view(), name='article-vote-list'),
    path('article-votes/<int:pk>', views.ArticleVoteDetail.as_view(), name='article-vote-detail'),

    path('news-votes/', views.NewsVoteList.as_view(), name='news-vote-list'),
    path('news-votes/<int:pk>', views.NewsVoteDetail.as_view(), name='news-vote-detail'),

    path('comment-votes/', views.CommentVoteList.as_view(), name='comment-vote-list'),
    path('comment-votes/<int:pk>', views.CommentVoteDetail.as_view(), name='comment-vote-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
