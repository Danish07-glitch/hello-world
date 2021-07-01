from django.urls import path
from blog import views

urlpatterns=[
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
    path('home/',views.BlogListView.as_view(),name='home'),
    path('',views.IndexView.as_view(),name='base'),

]
