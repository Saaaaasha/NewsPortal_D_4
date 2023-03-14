from django.urls import path
from .views import NewsList, PostDetail, PostSearch, PostCreate, PostDelete, PostUpdate

urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', PostSearch.as_view(), name='post_search'),
    path('create/', PostCreate.as_view(), name='news_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]
