from django.views import View
from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.conf import settings

from .models import Images

import datetime
import json

class HomeView(View):
    template_name = "index.html"

    def get(self, request):

        item = Images.objects.all().order_by('-datetime')
        return render(request, self.template_name, {'item': item})


class UploadView(View):

    def post(self, request):

        Images(image=request.FILES['image']).generate()
        return redirect('/')


class ImageView(View):

    def get(self, request, image):

        name = str(image)[:16]

        # full size request
        if len(name) == 16:
            image_file = Images.objects.filter(image__startswith=image)[0]
            return HttpResponse(image_file.image, content_type="image/png")

        # thumbnail request
        elif len( name ) == 8:
            image_file = Images.objects.filter(thumb__startswith=image)[0]
            return HttpResponse(image_file.thumb, content_type="image/png")


class APIBoardView(View):

    def get(self, request):

        return HttpResponse('gtg')


class SubscribeView(View):

    def get(self, request):

        item = Images.objects.all()

        """
        data = []
        for ea in item:
            data.append(ea.thumb.name[:8])
            print(ea.thumb.name[:8])
        """


        val = "data: {}\n\n".format(len(item))

        return HttpResponse(val, content_type="text/event-stream")

