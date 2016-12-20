from io import  BytesIO
from PIL import Image
import os

from django.db import models
from django.core.files.base import ContentFile

from .helper.generator import id_generator

from .helper.ImageModifiers import ImageModifiers


class Images(models.Model):

    image = models.FileField()
    thumb = models.FileField()
    datetime = models.DateTimeField(auto_now_add=True)

    def generate(self):
        self.name()
        self.thumbnail()

    def name(self):

        name, self.ext = os.path.splitext(self.image.name)
        self.image.name = id_generator(size=16)+self.ext.lower()

    def thumbnail(self):

        blarg = ImageModifiers.maxsize(self.image, lsize=150)

        self.thumb.name = id_generator(size=8) + self.ext.lower()
        self.thumb.file = ContentFile(blarg.read())
        self.thumb.save(self.thumb.name, self.thumb.file, save=True)



    def imagename(self):
        return str(self.image.name[:16])

    def thumbname(self):
        return str(self.thumb.name[:8])