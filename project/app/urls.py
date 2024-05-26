from django.urls import path
# from .views import normalapi
from .views import*
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    
    # ======= Normal API without Using DRF  ==============

   # path('list/', normalapi, name='normalapi'),

   # ================ Class based API ===========================
path('productlist/', Product_list.as_view(), name='product_list'),
path('productdetail/<int:pk>/', Product_detail.as_view(), name='product_detail'),






]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)