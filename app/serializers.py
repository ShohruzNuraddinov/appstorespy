import magic
from io import BytesIO
from rest_framework import serializers


from app import models
from app.tasks import image_resize
from app.utils import File


class ImageResizeSerializer(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = models.File
        fields = ('user', 'file')

    def create(self, validated_data):
        file = super().create(validated_data)
        file_url = file.file.url
        print(file.file.name)

        file_1 = File().image_resize(
            100000, file_url, 720)
        print(file_1)
        # print(file_url)
        return validated_data
