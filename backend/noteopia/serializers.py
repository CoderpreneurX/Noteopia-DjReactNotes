from .models import Note
from rest_framework import serializers

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        extra_kwargs = {
            'user': {'required': False}
        }

    def __str__(self):
        return f'{self.user.username} - {self.title}'