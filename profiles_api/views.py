from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self,request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'teste',
            'teste2',
            'teste3',
            'teste4',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})