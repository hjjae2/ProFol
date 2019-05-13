from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_redirect),
    # path('app/', views.index),
    path('app/login/', views.mng_login),

    path('app/', views.mng_personal),
    path('app/<int:pk>/', views.mng_project),
    path('app/<int:pk>/<str:category_title>/', views.mng_part),

    path('app/portfolio/', views.user_portfolio),
    path('app/portfolio_detail/<int:pk>/', views.user_portfolio_detail),

    # create prject, todolist
    path('app/create_project_form/', views.create_project_form),
    path('app/create_project/', views.create_project),

    # redirection
    path('app/done/<int:pk>', views.finish_todo),
    path('app/<int:pk>/<str:category_title>/done/<int:todo_pk>', views.finish_todo_part),
]