from django.views import View
from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.conf import settings

import copy

from .models import Images
from .helper import generator
from .helper.ImageModifiers import ImageModifiers


class HomeView(View):
    template_name = "index.html"
    def get(self, request):

        item = Images.objects.all().order_by('-datetime')
        return render(request, self.template_name, {'item':item})



class UploadView(View):

    def post(self, request):

        file = request.FILES['image']

        thumb = copy.deepcopy(file)


        file.name = '{}.png'.format(generator.id_generator(size=16))
        file.file = ImageModifiers.maxsize(file, 1000)

        thumb.name = '{}.png'.format(generator.id_generator(size=8))
        thumb.file = ImageModifiers.thumbnailer(file)


        Images(image=file, thumb=thumb).save()

        return redirect('/')


class ImageView(View):

    def get(self, request, image):
        try:

            if len(image) == 16:

                image_file = Images.objects.filter(image='{}.png'.format(image))[0]
                return HttpResponse(image_file.image, content_type="image/png")

            else:

                image_file = Images.objects.filter(thumb='{}.png'.format(image))[0]
                return HttpResponse(image_file.thumb, content_type="image/png")


        except:
            return redirect('/')
