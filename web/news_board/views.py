from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class Upvotes(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        serializer = PostSerializer(post)
        return Response({"posts": serializer.data})

    def patch(self, request, pk):
        model = get_object_or_404(Post, id=pk)
        data = {"amount_of_upvotes": model.amount_of_upvotes + 1}
        serializer = PostSerializer(model, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
