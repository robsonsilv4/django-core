from django.shortcuts import render
from django.http import HttpResponse

from .models import PostModel


def post_model_list_view(request):
    qs = PostModel.objects.all()
    print(qs)
    # return HttpResponse('Some Object...')
    template = 'blog/list-view.html'
    context = {
        'object_list': qs,
        'test': 'Hello, from context!'
    }
    return render(request, template, context)
