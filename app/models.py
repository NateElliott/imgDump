from django.db import models


class Images(models.Model):

    image = models.FileField()
    thumb = models.FileField()
    datetime = models.DateTimeField(auto_now_add=True)

    def thumbnail(self):
        return str(self.thumb)[:8]

    def __str__(self):
        return str(self.image)[:16]

