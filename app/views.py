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

        Images(image=request.FILES['image']).generate()

        return redirect('/')


class ImageView(View):

    def get(self, request, image):

        # full size request
        if len(image)==16:
            image_file = Images.objects.filter(image__startswith=image)[0]
            return HttpResponse(image_file.image, content_type="image/png")

        # thumbnail request
        elif len(image)==8:
            image_file = Images.objects.filter(thumb__startswith=image)[0]
            return HttpResponse(image_file.thumb, content_type="image/png")

