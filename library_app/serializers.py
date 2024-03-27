from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Rental

class RentalSerializer(ModelSerializer):
    a_client = SerializerMethodField(read_only=True)
    a_book = SerializerMethodField(read_only=True)
    
    class Meta:
        model = Rental
        fields = '__all__'
    
    def get_a_client(self, instance):
        client = instance.a_client.all()
        ser_client = [{'username': x.username} for x in client]
        return ser_client
    
    def get_a_book(self, instance):
        book = instance.a_book.all()
        ser_book = [{'title': x.title} for x in book]
        return ser_book