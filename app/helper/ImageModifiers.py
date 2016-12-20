import os

from io import BytesIO
from PIL import Image


class ImageModifiers:


    def maxsize(image, lsize):

        im = Image.open(image)

        size = (lsize, lsize)
        im.thumbnail(size, Image.ANTIALIAS)
        name, ext = os.path.splitext(image.name)

        if ext in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif ext == '.gif':
            FTYPE = 'GIF'
        elif ext == '.png':
            FTYPE = 'PNG'
        else:
            raise Exception('unknown file type')

        buffer = BytesIO()
        im.save(buffer, format=FTYPE)
        buffer.seek(0)

        return buffer


    def thumbnailer(image, lsize=200, quality=25):

        im = Image.open(image)

        size = (lsize,lsize)
        im.thumbnail(size, Image.ANTIALIAS)

        hw = im.size[0]/2
        hl = im.size[1]/2
        hs = lsize/2

        crop = im.crop(
            (
                hw-hs,
                hl-hs,
                hw+hs,
                hl+hs
            )
        )

        buffer = BytesIO()
        crop.save(buffer, format='JPEG', optimize=True, quality=quality)

        return buffer
