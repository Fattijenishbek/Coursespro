from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Course, Branch, Contact
from .serializer import CourseSerializer, BranchSerializer, ContactSerializer

# Create your views here.
class CourseViewSet(ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer


class BranchViewSet(ModelViewSet):
    queryset=Branch.objects.all()
    serializer_class=BranchSerializer


class ContactViewSet(ModelViewSet):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer

