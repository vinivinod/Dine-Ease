"""
URL configuration for DineEase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home.views import userlogin,register,loggout,login_page

from home.views import index,menu,about,menumore,add_table,add_reservation,booking_confirm,cancel_reservation,edit_reservation,res_list
from home.views import payment,paymenthandler,book_table,cart,add_to_cart,view_cart,remove_from_cart,update_cart_item_quantity,checkout,display_cart_items
from home.views import admin_login,admin_index,add_menu,user_list,ad_MenuList,menu_list,menu_edit,delete_menu_item
from home.views import emp_leave,emp_index,emp_add,emp_profile,emp_list,emp_edit,products_by_category,filtered_menus,emp_registration,save_employee_details,employee_profile,delete_emp,change_pswrd
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name=''),
    path('menu/',menu,name='menu'),
    path('about/',about, name='about'),
    # path('book/',book,name='book'),
    path('menumore/',menumore, name='menumore'),
    path('register/',register,name='register'),
    path('login/', login_page, name='login'),
    path('login-submit/', userlogin, name='login-submit'),
    
    path('loggout', loggout, name='loggout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path("",include("allauth.urls")),
    path('home/',include('home.urls')),
    path('add_table/', add_table, name='add_table'),
    path('add_reservation/', add_reservation, name='add_reservation'),
    path('booking_confirm/',booking_confirm, name='booking_confirm'),
    path('booking_confirm/<int:menu_id>/',booking_confirm, name='booking_confirm'),
    path('cancel_reservation/<str:reservation_id>/', cancel_reservation, name='cancel_reservation'),
    path('edit_reservation/<str:reservation_id>/', edit_reservation, name='edit_reservation'),
    path('res_list/',res_list,name='res_list'),
    path('book_table/', book_table, name='book_table'),
    path('cart/',cart, name='cart'),
    path('add_to_cart/<int:menu_id>/',add_to_cart,name='add_to_cart'),
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('update_cart_item_quantity/<int:item_id>/<int:new_quantity>/', update_cart_item_quantity, name='update_cart_item_quantity'),
    path('view_cart/', view_cart, name='view_cart'),
    path('checkout/',checkout,name='checkout'),
    path('payment/<int:billing_id>/', payment, name='payment'),
    path('paymenthandler/<int:billing_id>/', paymenthandler, name='paymenthandler'),
    path('display_cart_items',display_cart_items,name='display_cart_items'),
    

    path('admin_login/',admin_login,name='admin_login'),
    path('admin_index/',admin_index,name='admin_index'),
    # path('ad_MenuAdd/',ad_MenuAdd,name='ad_MenuAdd'),
    
    path('add_menu/', add_menu, name='add_menu'),
    path('ad_MenuList/',ad_MenuList,name='ad_MenuList'),
   
    path('menu_list/', menu_list, name='menu_list'),
    path('user_list',user_list,name='user_list'),
    path('menu_edit/<int:menu_id>/', menu_edit, name='menu_edit'),
    path('delete_menu_item/<int:menu_id>/',delete_menu_item,name='delete_menu_item'),

    path('emp_registration',emp_registration,name='emp_registration'),
    path('emp_index/',emp_index, name='emp_index'),
    path('emp_add/',emp_add, name='emp_add'),
    path('emp_edit/<int:emp_id>/',emp_edit, name='emp_edit'),
    path('emp_list/',emp_list, name='emp_list'),
    path('delete_emp/<int:emp_id>/',delete_emp,name='delete_emp'),
    path('emp_profile/',emp_profile, name='emp_profile'),
    path('employee_profile/',employee_profile,name='employee_profile'),
    path('save_employee_details',save_employee_details,name='save_employee_details'),
    path('change_pswrd/',change_pswrd,name='change_pswrd'),
    path('products/<str:category_name>/', products_by_category, name='products_by_category'),
    path('filtered-menus/<str:category>/<str:submenu>/<str:sub_submenu>/', filtered_menus, name='filtered_menus'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

