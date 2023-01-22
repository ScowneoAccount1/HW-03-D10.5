from django.urls import path
from .views import PostList, PostDetail, SearchList, AddList, PostUpdateView, PostDeleteView
from .views import upgrade_me, subscribe_categories
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view()), #! path for 'macdonalds' or D10
    # path('', PostList.as_view()), #* normal path
    path('<int:pk>', PostDetail.as_view(), name='product_detail'),
    path('search/', SearchList.as_view()),
    path('add/', AddList.as_view()),
    path('<int:pk>/edit', PostUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='product_delete'),
    path('upgrade/', upgrade_me, name='upgrade'),
    path('subscribe/', subscribe_categories),
]
