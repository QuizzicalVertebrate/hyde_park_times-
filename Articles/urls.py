from django.urls import path
from .views import (
    
    ArticleDeleteView,
    ArticleListView, 
    ArticleDetailView,
    ArticleCreateView, 
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleListView,
)


urlpatterns = [

    path('', ArticleListView.as_view(), name = 'ArticleListView' ),
    path('detail/<int:pk>/', ArticleDetailView.as_view(), name='Article_detail'),
    path('new/', ArticleCreateView.as_view(), name='Article-create'),
    path('<int:pk>/update/', ArticleUpdateView.as_view(), name='ArticleUpdateView'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='Article-delete'),
]