from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import get_magic_number
from .serializers import MagicNumberSerializer


class MagicNumberView(APIView):
    serializer_class = MagicNumberSerializer

    def get(self, request):
        magic_number = get_magic_number()
        serializer = self.serializer_class(magic_number)
        return Response(serializer.data, status=status.HTTP_200_OK)
