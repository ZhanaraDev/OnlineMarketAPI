from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response

from mainapp.models import Product
from .serializers import UserSerializer, GroupSerializer, ProductSerializer
from .permissions import CustomPermission

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (CustomPermission,)

    def check_permissions(self, request):
        super().check_permissions(request)

    def dispatch(self, request, *args, **kwargs):
        if request.method == "DELETE" and not kwargs:
            Product.objects.all().delete()
            return JsonResponse({'message': 'Everything was deleted'}, status=200)

        return super().dispatch(request, *args, **kwargs)




