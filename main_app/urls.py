from django.urls import path
from . import views

urlpatterns = [
    path('' , views.homepage, name='homepage'),
    #path('items/' , views.item_list, name='item_list'),
    #path('my-items/' , views.item_list_personal, name='item_list_personal'),
    #path('items/<int:id>/',views.item_details, name='item_details'),
    path('items/',views.item_list, name='item_list'),
    path('my-items/',views.item_list_personal, name='my_item_list'),
    path('items/<int:id>/',views.item_details, name='item_details'),
    path('my-items/<int:id>/',views.my_item_details, name='my_item_details'),
    path('items/create', views.create_item, name='item_create'),
    path('items/<int:id>/edit', views.update_item, name='edit_item'),
    path('items/<int:id>/delete',views.delete_item, name='delete_item'),
    path('categories/',views.category_list, name='category_list'),
    path('categories/<int:id>/',views.category_details, name='category_details'),
    path('categories/create/', views.create_category, name='create_category'),
    path('auth/signup/', views.SignUpView.as_view(), name='signup')

]

