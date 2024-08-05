from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Note
from .serializers import NoteSerializer

class ListCreateNoteAPIView(generics.ListCreateAPIView):
    # queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        try:
            notes = Note.objects.filter(user=user).all().order_by('-created_at')
            return notes
        except Note.DoesNotExist:
            notes = Note.objects.none()
            return notes
        
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
        return serializer

class RetrieveUpdateDeleteNoteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]