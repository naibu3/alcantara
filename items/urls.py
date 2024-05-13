from django.urls import path
from items import views

urlpatterns = [
    path('', views.index, name='index'),
    #CREATE ITEM
    path('create-item-form/', views.create_item_form, name='create-item-form'),
    path('create-item/', views.create_item, name='create-item'),
    #LIST ALL ITEMS
    path('list-items/', views.list_items, name='list-items'),
    #SEARCH ITEMS
    path('search-items/', views.search_items, name='search-items'),
    #EDIT ITEMS
    path('delete-item/', views.delete_item, name='delete-item'),
    path('update-item-form/<str:name>/', views.update_item_form, name='update-item-form'),
    path('update-item/', views.update_item, name='update-item')
]

handler404 = 'items.views.custom_page_not_found'