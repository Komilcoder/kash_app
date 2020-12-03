from django.shortcuts import render
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status,generics,permissions
from .serializers import NewsSerializer
from .models import News



class NewsListView(APIView):
    """
    List and CreateViews 
    """

    permission_classes = [IsAuthenticated]

    def get(self,request, format=None):
        query = News.objects.all()
        serializer = NewsSerializer(query,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsDetailView(APIView):
    """
    Retrieve , Update and DeleteViews:
    """

    permission_classes = [IsAuthenticated]

    def get_object(self,pk):
        try:
            return News.objects.get(id=pk)
        except News.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        query = self.get_object(pk)
        serializer = NewsSerializer(query)
        return Response(serializer.data) 

    def put(self, request, pk,format=None):
        query = self.get_object(pk)
        serializer = NewsSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk,format=None):
        query = self.get_object(pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
                       

