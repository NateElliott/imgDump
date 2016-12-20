from django.db import models
import os
from django.core.files.storage import default_storage as storage
from django.core.files.base import ContentFile

from django.conf import settings as settings

from PIL import Image

from .helper.generator import id_generator

from io import StringIO, BytesIO


class Images(models.Model):

    image = models.FileField()
    thumb = models.FileField()
    datetime = models.DateTimeField(auto_now_add=True)

    def abc(self):

        name, self.ext = os.path.splitext(self.image.name)

        self.image.name = id_generator(size=16)+self.ext.lower()


    def save(self, *args, **kwargs):

        super(Images, self).save(*args, **kwargs)


    def thumbnail(self):

        im = Image.open(self.image)

        im.thumbnail((180,180), Image.ANTIALIAS)

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

