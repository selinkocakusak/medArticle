from django.urls import path
from . import views


# SET THE NAMESPACE!
app_name = 'medApp'

urlpatterns = [
    path('search_results/', views.search_results, name='search_results'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('search/', views.search, name='search'),
    path('article/<int:doc_id>/', views.article, name='article'),
    path('tag/', views.tag, name='tag'),
    path('wikidatasearch/', views.get_wikidata, name='get_wikidata'),
    path('', views.home, name='home'),
    path('user_logout/', views.user_logout, name='user_logout'),



]
