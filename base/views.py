from django.http import  HttpResponse
from django.contrib.auth.models import User
# from .serializers import ProductSerializer
# from .models import Product
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes,api_view


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
 
        # Add custom claims
        token['username'] = user.username
        # ...
 
        return token
 
 
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    # register
@api_view(['POST'])
def register(request):
    user = User.objects.create_user(
                username=request.data['username'],
                email=request.data['email'],
                password=request.data['password']
            )
    user.is_active = True
    user.is_staff = True
    user.save()
    return Response("new user born")


# @permission_classes([IsAuthenticated])
# class ProductView(APIView):
#     def get(self, request):
#         my_model = Product.objects.all()
#         serializer = ProductSerializer(my_model, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data, context={'user': request.user})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
#     def put(self, request, pk):
#         my_model = Product.objects.get(pk=pk)
#         serializer = ProductSerializer(my_model, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
#     def delete(self, request, pk):
#         my_model = Product.objects.get(pk=pk)
#         my_model.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

def index(req):
    return HttpResponse('<h1>hello')
