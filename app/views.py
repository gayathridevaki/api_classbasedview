from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from app.serializers import * 

# Create your views here.
class productcrud(APIView):
    def get(self,request,id):
        PDO=product.objects.all()
        #PDO=product.objects.get(id=id)
        PJO=productmodelserializer(PDO,many=True)
        return Response(PJO.data)
    
    def post(self,request,id):
        JOD=request.data#json data
        PDO=productmodelserializer(data=JOD)#orm data
        if PDO.is_valid():
            PDO.save()
            return Response({'insert':'data inserted successfully'})
        else:
            return Response({'error':'data is not inserted successfully'})
        
    def put(self,request,id):
        PO=product.objects.get(id=id)
        UPDO=productmodelserializer(PO,data=request.data)
        if UPDO.is_valid():
            UPDO.save()
            return Response({'update':'data is updated'})
        else:
            return Response({'error':'data is not updated'})
        

    def patch(self,request,id):
        PO=product.objects.get(id=id)
        UPDO=productmodelserializer(PO,data=request.data,partial=True)
        if UPDO.is_valid():
            UPDO.save()
            return Response({'update':'data is updated'})
        else:
            return Response({'error':'data is not updated'})
        
    def delete(self,request,id):
        product.objects.get(id=id).delete()
        return Response({'data':'data is deleted'})

        
    