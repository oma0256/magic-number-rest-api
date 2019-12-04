from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import get_magic_number
from .serializers import MagicNumberSerializer
from .permissions import HasPermission


class MagicNumberView(APIView):
    serializer_class = MagicNumberSerializer
    permission_classes = [HasPermission]

    def get(self, request):
        magic_number = get_magic_number()
        serializer = self.serializer_class(magic_number)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        magic_number = get_magic_number()
        if magic_number is None:
            return Response({"error": "There's no magic number"},
                            status=status.HTTP_404_NOT_FOUND)
        data = request.data
        serializer = self.serializer_class(magic_number, data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
