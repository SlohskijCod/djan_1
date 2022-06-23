from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('cont/', views.cont, name='cont'),
    path('one/', views.one, name='one'),
    path('catalog/', views.cat, name='catalog'),
    path('xboxseriesx/', views.hh1, name='hh1'),
    path('PlayStation5/', views.hh2, name='hh2'),
    path('XboxOneX/', views.hh3, name='hh3'),
    path('PlayStation4/', views.hh4, name='hh4')
]
