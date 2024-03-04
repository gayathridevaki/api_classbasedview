from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from app.serializers import * 

# Create your views here.
class productcrud(APIView):
    def get(self,request):
        PDO=product.objects.all()
        PJO=productmodelserializer(PDO,many=True)
        return Response(PJO.data)
    
    def post(self,request):
        JOD=request.data#json data
        PDO=productmodelserializer(data=JOD)#orm data
        if PDO.is_valid():
            PDO.save()
            return Response({'insert':'data inserted successfully'})
        else:
            return Response({'error':'data is not inserted successfully'})