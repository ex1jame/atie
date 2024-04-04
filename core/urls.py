from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from rest_framework import permissions
from rest_framework.routers import SimpleRouter

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from order.views import OrderAPIView
from category.views import CategoryViewSet
from product.views import ProductViewSet
from review.views import ReviewViewSet

router = SimpleRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)
router.register('reviews', ReviewViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Blog Test",
      default_version='v1',
      description="Atie",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny,],
)


urlpatterns = [
    path('docs<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('account.urls')),
    path('api/v1/orders/', OrderAPIView.as_view()),
    path('api/v1/', include(router.urls)),



]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)