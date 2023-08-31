"""
URL configuration for skincare_app project.

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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from product.views import home_page,catalog_page,product_preview,add_product
from user.views import user_login,user_logout,register
from cart.views import cart,cart_add

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page),
    path('catalog',catalog_page),
    path('product/<int:id>',product_preview),
    path('product/add',add_product),
    path('login',user_login),
    path('cart',cart),
    path('register',register),
    path('logout',user_logout),
    path('cart/add/<int:id>',cart_add)
    # path('cart/checkout',)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()