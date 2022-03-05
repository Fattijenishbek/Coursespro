from django.urls import path, include
from rest_framework import  routers
from .views import CourseViewSet, BranchViewSet, ContactViewSet

router=routers.DefaultRouter()
router.register('courses', CourseViewSet)
router.register('branches', BranchViewSet)
router.register('contacts', ContactViewSet)

urlpatterns=[
    path('', include(router.urls))
]