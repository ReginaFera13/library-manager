from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import (
    HTTP_200_OK, 
    HTTP_201_CREATED, 
    HTTP_204_NO_CONTENT, 
    HTTP_400_BAD_REQUEST
)
from .serializers import RentalSerializer, Rental

# Create your views here.
class All_rentals(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = self.request.user
        rentals = Rental.objects.filter(a_client=user).order_by('id')
        ser_rentals = RentalSerializer(rentals, many=True)
        return Response(ser_rentals.data, status=HTTP_200_OK)
    
    def post(self, request):
        data = request.data.copy()
        pending_rental = RentalSerializer(data=data)
        if pending_rental.is_valid():
            pending_rental.save()
            return Response(pending_rental.data, status=HTTP_201_CREATED)
        return Response(pending_rental.errors, status=HTTP_400_BAD_REQUEST)


class A_rental(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id):
        rental = get_object_or_404(Rental, id=id)
        ser_rental = RentalSerializer(rental)
        return Response(ser_rental.data, status=HTTP_200_OK)
    
    def put(self, request, id):
        rental = get_object_or_404(Rental, id=id)
        ser_rental = RentalSerializer(rental, data=request.data)
        if ser_rental.is_valid():
            ser_rental.save()
            return Response(ser_rental.data)
        return Response(ser_rental.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        rental = get_object_or_404(Rental, id=id)
        rental.delete()
        return Response(status=HTTP_204_NO_CONTENT)