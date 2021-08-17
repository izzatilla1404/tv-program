from django.shortcuts import render
from django.views.generic import View
from .models import Category, Channel, Program
from django.utils.translation import gettext_lazy as _


class MainIndex(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = _("TVDASTUR")

    def get(self, request):
        return render(request, 'main/index.html', {
            'category': Category.objects.all(),
            'channel': Channel.objects.order_by('-id').all(),
            'program': Program.objects.all()
        })


class CategoryView(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

    def get(self, request, gid=None):
        p = request.GET.get('p', '')
        if gid is None:
            channel = Channel.objects.filter(Channel_name__icontains=p).all()
        else:
            channel = Channel.objects.filter(Category=gid, Channel_name__icontains=p).all()
        return render(request, 'main/index.html', {
            'category': Category.objects.all(),
            'channel': channel,
            'program': Program.objects.all()
        })


class ChannelView(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'main/index.html')


class ProgramView(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, *kwargs)

    def det(self, request):
        return render(request, 'main/index.html')
