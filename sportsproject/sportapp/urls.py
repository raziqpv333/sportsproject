from django.urls import path
from . import views

urlpatterns=[
    path('home',views.home),
    path('',views.login),
    path('registration/',views.registration),
    path('contact/', views.contact_view, name='contact'),  # Ensure this view exists
    path('products/', views.products_view, name='products'),
    path('about/', views.about_view, name='about'),
    # path('home/',views.home_view, name='home'),
    path('viewproduct/<int:id>/', views.viewproduct, name='viewproduct'),
    path('logout/', views.logout),
    path('cartdis/',views.cartdisplay),
    path('addtocart/<int:id>',views.addtocart),
    path('ingrement/<int:id>',views.ingrement),
    path('degrement/<int:id>',views.degrement),
    path("delete/<id>",views.delete_cart),
    # path('buy/<int:id>',views.buy),
    path('address/<int:id>/<int:cid>',views.address_info,name='addressinfo'),
    path("delete/<cid>",views.delete),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('cancel_order/<int:id>',views.cancel_order,name='cancel_orders')


 

    # path('viewproduct/<id>',views.viewproduct)


]