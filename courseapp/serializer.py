from unicodedata import category
from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['name', 'imagepath']

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Branch
        fields=['latitude','longitude','address']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields=['type','value']

class CourseSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    contacts=ContactSerializer(many=True, source='contact_set')
    branches=BranchSerializer(many=True, source='branch_set')

    class Meta:
        model=Course
        fields=['name','description','logo', 'category','contacts','branches']

    def create(self, validate_data):
        contacts=validate_data.pop('contact_set')
        branches=validate_data.pop('branch_set')
        category=validate_data.pop('category')

        category=Category.objects.create(**category)
        course=Course.objects.create(**validate_data, category=category)

        for contact in contacts:
            c=Contact.objects.create(course_id=course, **contact)

        for branch in  branches:
            b=Branch.objects.create(course_id=course, **branch)

        return course

