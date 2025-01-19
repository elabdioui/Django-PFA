from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name="home"),


    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('contact/',views.contact,name="contact"),

    path('products/', views.list_products, name="product_list"),
    path('fproducts/', views.filterproduit, name='fproduct'),
    path('products/<int:id>/', views.product_detail, name='product_detail'),

         
    path('signup/', views.signup_or_login, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.signup_or_login, name='login'),

    path('cart/',views.get_cart,name="my_cart"),
    path('add_cart/<int:product_id>',views.add_to_cart,name="add_to_cart"),
    path('add_cart/<int:product_id>/<int:quantity>',views.add_to_cart,name="add_to_cart_qte"),
    path('update_cart/<int:product_id>/<int:quantity>',views.add_to_cart,name="update_cart"),
    path('delete_cart/<int:product_id>',views.delete_from_cart,name="delete_cart"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
