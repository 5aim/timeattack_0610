from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')), # 리스트 형태로 products의 urls list가 더해지는 것임.
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)