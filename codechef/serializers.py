from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
 class Meta:
  model = Student
  fields = ['username', 'rating', 'highest_rating','global_rank','country_rank']


