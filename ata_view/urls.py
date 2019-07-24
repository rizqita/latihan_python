from django.urls import path
from . import views

urlpatterns = [
    path('',views.ata_view_main,name='ata_view_main'),
    path('mentor',views.mentor_view,name='mentor'),
    path('mentee',views.mentee_view,name='mentee'),
    path('author',views.author_view,name='author'),
    path('blog',views.blog_view,name='blog'),
    path('input_mentee',views.input_mentee,name='input_mentee'),
    path('input_mentor',views.input_mentor,name='input_mentor'),
    path('input_blog',views.input_blog,name='input_blog')
]