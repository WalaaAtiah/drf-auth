
from rest_framework import serializers
# Create your views here.
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
   class Meta:
       model= Movie
       # fields=['id','name', 'owner', 'description'] # see specific field 
       fields='__all__'