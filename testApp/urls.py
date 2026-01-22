from django.urls import path
from . import views

urlpatterns = [
    # レビュー一覧＋投稿
    path('reviews/', views.review_list, name='review_list'),

    # レビュー削除
    path('reviews/delete/<int:pk>/', views.review_delete, name='review_delete'),

    # レビュー編集
    path('reviews/edit/<int:pk>/', views.review_edit, name='review_edit'),
]
