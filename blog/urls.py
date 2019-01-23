from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('post/<id>', views.view_post, name="post"),
    path('about/',views.about,name='about_us'),
    path('contact',views.contact,name='contact'),
    path('edit-post/<id>',views.edit_post,name='edit-post'),
    path('delete/<id>',views.delete,name='delete'),
    path('create-post/',views.create_post,name='create-post'),
    path('search',views.search,name='search'),
    path('my-post', views.my_post, name='my_post')
]