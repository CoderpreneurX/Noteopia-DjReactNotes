from django.urls import path
from .views import ListCreateNoteAPIView, RetrieveUpdateDeleteNoteAPIView

urlpatterns = [
    path('', ListCreateNoteAPIView.as_view(), name='list-create-notes'),
    path('note/<int:pk>/get-update-delete/', RetrieveUpdateDeleteNoteAPIView.as_view(), name='retrieve-update-delete-note'),
]