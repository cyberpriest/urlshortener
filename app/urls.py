
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='homepage'),
    path('create/',views.Create,name='create'),
    path('<str:pk>',views.go_func,name='go')

]

app_name ='app'
