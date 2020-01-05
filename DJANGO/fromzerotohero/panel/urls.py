from django.urls import path
from panel import views

app_name = 'panel'

urlpatterns = [
    path('', views.home, name='home'),
    path('news/list', views.news_list, name='news_list'),
    path('news/add', views.news_add, name='news_add'),
    path('news/delete/<int:pk>', views.news_delete, name='news_delete'),
    path('news/edit/<int:pk>', views.news_edit, name='news_edit'),
    path('category/delete/<int:pk>', views.category_delete, name='category_delete'),
    path('category/list/', views.category_list, name='category_list'),
    path('category/add/', views.category_add, name='category_add'),
    path('subcategory/delete/<int:pk>', views.subcategory_delete, name='subcategory_delete'),
    path('subcategory/list/', views.subcategory_list, name='subcategory_list'),
    path('subcategory/add/', views.subcategory_add, name='subcategory_add'),
    path('sitesettings/', views.site_settings, name='site_settings'),
    path('message_box/', views.message_box, name='message_box'),
    path('trends/list', views.trends, name='trends_list'),
    path('trends/delete/<int:pk>', views.trends_delete, name='trends_delete'),
    path('trends/update/<int:pk>', views.trends_update, name='trends_update'),
    path('trends/add/', views.trend_add, name='trends_add'),
    path('users/change_password/', views.change_pass, name='change_password'),
    path('users/managers/list/', views.manager_list, name='manager_list'),
    path('users/managers/delete/<int:pk>/', views.manager_del, name='manager_delete'),
    path('users/managers/group/list/', views.manager_group_list, name='manager_group_list'),
    path('users/managers/group/add/', views.manager_group_add, name='manager_group_add'),
    path('users/managers/group/delete/<int:pk>/', views.manager_group_del, name='manager_group_delete'),
    path('users/groups/<int:pk>/', views.users_groups, name='users_groups'),
    path('users/groups/add/<int:pk>/', views.users_groups_add, name='users_groups_add'),
    path('users/groups/delete/<int:uid>/<int:gid>/', views.users_groups_delete, name='users_groups_delete'),
    path('users/permissions/list/', views.permission_list, name='permission_list'),
    path('users/permissions/delete/<int:pk>/', views.permission_delete, name='permission_delete'),
    path('users/permissions/user/permission/<int:pk>/', views.users_perms, name='users_permissions'),
    path('users/permissions/user/permission/delete/<int:uid>/<int:pid>/', views.users_perms_delete,
         name='users_permissions_delete'),
    path('users/permissions/user/permission/add/<int:uid>/', views.users_perms_add,
         name='users_permissions_add'),
    path('users/permissions/group/permission/<int:pk>/', views.group_perms, name='group_permissions'),
    path('users/permissions/group/permission/delete/<int:gid>/<int:pid>/', views.group_perms_delete,
         name='group_permissions_delete'),
    path('users/permissions/group/permission/add/<int:gid>/', views.group_perms_add,
         name='group_permissions_add'),
]
