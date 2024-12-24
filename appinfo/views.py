from rest_framework import status 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from .models import AppData 
from .serializers import AppSerializer 

# Create your views here.

@api_view(['POST']) 
def add_app(request): 
    serializer = AppSerializer(data=request.data) 
    if serializer.is_valid(): 
        serializer.save()  
        return Response(serializer.data,status=status.HTTP_201_CREATED) 
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET']) 
def get_app(request,id): 
    try: 
        app = AppData.objects.get(pk=id) 
    except AppData.DoesNotExist: 
        return Response({'error':'App not found'},status=status.HTTP_404_NOT_FOUND) 
    serializer = AppSerializer(app) 
    return Response(serializer.data) 

@api_view(['DELETE']) 
def delete_app(request,id): 
    try: 
        app = AppData.objects.get(pk=id) 
    except AppData.DoesNotExist: 
        return Response({'error':"App not found"},status=status.HTTP_404_NOT_FOUND) 
    app.delete() 
    return Response({'Message':'App deleted successfully!'},status=status.HTTP_204_NO_CONTENT)  


