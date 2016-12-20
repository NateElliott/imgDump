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
        image = request.FILES['image']



        test = Images(image=image)
        test.abc()
        test.thumbnail()

        test.save()

        return redirect('/')


class ImageView(View):

    def get(self, request, image):
        image_file = Images.objects.filter(image=image+'.jpg')[0]
        return HttpResponse(image_file.image, content_type="image/png")
