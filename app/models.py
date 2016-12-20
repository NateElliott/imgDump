from io import  BytesIO
from PIL import Image
import os

from django.db import models
from django.core.files.base import ContentFile

from .helper.generator import id_generator


class Images(models.Model):

    image = models.FileField()
    thumb = models.FileField()
    datetime = models.DateTimeField(auto_now_add=True)

    def name(self):

        name, self.ext = os.path.splitext(self.image.name)
        self.image.name = id_generator(size=16)+self.ext.lower()

    def thumbnail(self):

        im = Image.open(self.image)
        im.thumbnail((150,150), Image.ANTIALIAS)


        if self.ext in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif self.ext == '.gif':
            FTYPE = 'GIF'
        elif self.ext == '.png':
            FTYPE = 'PNG'
        else:
            raise Exception('unknown file type')

        buffer = BytesIO()
        im.save(buffer, format=FTYPE)
        buffer.seek(0)

        self.thumb.name = id_generator(size=8) + self.ext.lower()
        self.thumb.file = ContentFile(buffer.read())
        self.thumb.save(self.thumb.name, self.thumb.file, save=True)

        buffer.close()


    def imagename(self):
        return str(self.image.name[:16])

    def thumbname(self):
        return str(self.thumb.name[:8])