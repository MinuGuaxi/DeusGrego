from django.urls import path
from DeusGrego import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('treinos/', views.treinos, name='treinos'),
    path('desafios/', views.desafios, name='desafios'),
    path('receitas/', views.receitas, name='receitas')
]