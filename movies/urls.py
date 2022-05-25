from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    # 감정 선택
    path('selectmood/', views.select_mood, name='select_mood'),

    # 리뷰 작성, 수정, 삭제
    path('create/<str:movie_pk>/', views.create, name='create'),
    path('read/<str:review_pk>/', views.read, name='read'),
    path('update/<str:review_pk>/', views.update, name='update'),
    path('delete/<str:review_pk>/', views.delete, name='delete'),

    # 감정별 영화 추천
    path('index/<str:mood_pk>/', views.index, name='index'),
    # 영화 상세 페이지
    path('<str:movie_pk>/', views.detail, name='detail'),
    # 영화 북마크
    path('<str:movie_pk>/save/', views.save, name='save'),
    # 영화 리뷰 좋아요
    path('<str:review_pk>/like/', views.review_like, name='review_like'),

    # path('commentcreate/<str:review_pk>/', views.commentcreate, name='commentcreate'),

    # path('commentupdate/<str:review_pk>/', views.commentupdate, name='commentupdate'),
    # path('commentread/<str:review_pk>/', views.commentread, name='commentread'),
    # path('commentdelete/<str:review_pk>/', views.commentdelete, name='commentdelete')
    
]
