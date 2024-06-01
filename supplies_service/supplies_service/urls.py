from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from supplies.views import PharmaceuticalViewSet, MedicalSupplyViewSet

router = DefaultRouter()
router.register(r'pharmaceuticals', PharmaceuticalViewSet)
router.register(r'medical-supplies', MedicalSupplyViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
