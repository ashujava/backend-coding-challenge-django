from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework import generics
from django.db.models import Q
from .models import Note
from .serializers import NoteSerializer
from .permissions import IsOwner
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny


class NotesView(mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
    """
    If logged in, Users can add, delete and modify their notes
    """
    permission_classes = (IsAuthenticated, IsOwner,)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class NotesListView(APIView):
    """
    - Users can see a list of all their notes
    - Notes can be either public or private
    - Public notes can only be viewed without authentication
    """

    def get(self, request, *args, **kwargs):
        note_objs = Note.objects.filter(owner=request.user.id) \
            if request.user.is_authenticated and Note.objects.filter(is_deleted=False) \
            else Note.objects.filter(is_public=True)
        serializer = NoteSerializer(note_objs, many=True)
        return Response(serializer.data)


class NotesFilterView(APIView):
    """
    Users can filter their notes via tags
    """
    permission_classes = (IsOwner,)

    def get(self, request, *args, **kwargs):
        tags = kwargs.get('tags', None)
        if tags:
            note_objs = Note.objects.filter(owner=request.user.id, **kwargs)
            serializer = NoteSerializer(note_objs, many=True)
            return Response(serializer.data)


class NotesSearchView(APIView):
    """
    Users can search contents of notes with keywords
    """
    permission_classes = (IsOwner,)

    def get(self, request, *args, **kwargs):
        keyword = kwargs.get('keyword', None)
        if keyword:
            note_objs = Note.objects.filter(Q(title__icontains=keyword) |
                                            Q(body__icontains=keyword) |
                                            Q(tags__icontains=keyword))
            serializer = NoteSerializer(note_objs, many=True)
            return Response(serializer.data)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

