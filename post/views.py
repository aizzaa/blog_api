from rest_framework.views import APIView
from .models import Category
from .serializers import CategorySerializer
from rest_framework.response import Response



class CategoryView(APIView):
    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        # serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


class CategoryDetailView(APIView):
    def get_object(self, pk, http404=None):
        try:
            return Category.objects.get(slug=pk)
        except Category.DoesNotExist:
            raise http404

    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(instance=category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=206)

    def delete(self, pk, request):
        category = self.get_object(pk)
        category.delete()
        return Response('It was deleted', status=204)

