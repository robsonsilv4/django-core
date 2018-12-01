from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required

from .models import PostModel


def post_model_detail_view(request, id=None):
    print(id)

    # obj = PostModel.objects.get(id=1)

    # try:
    #     obj = PostModel.objects.get(id=1)
    # except:
    #     raise Http404

    # qs = PostModel.objects.filter(id=100)
    # obj = None
    # if not qs.exists() qs.count() != 1:
    #     raise Http404
    # else:
    #     obj = qs.first()

    obj = get_object_or_404(PostModel, id=id)
    # print(obj.title)

    template = 'blog/detail-view.html'
    context = {'object': obj}

    return render(request, template, context)


def post_model_list_view(request):
    qs = PostModel.objects.all()

    template = 'blog/list-view.html'
    context = {
        'object_list': qs
    }

    return render(request, template, context)


@login_required(login_url='/login/')
def login_required_view(request):
    qs = PostModel.objects.all()
    print(qs)

    template = 'blog/list-view.html'
    context = {
        'object_list': qs,
        'test': 'Hello, from context!'
    }

    print(request.user)
    if request.user.is_authenticated:
        template = 'blog/list-view.html'
        print('Logged In!')
    else:
        template = 'blog/list-view-public.html'
        # print('Not Logged In!')
        # raise Http404
        return HttpResponseRedirect('/login')

    return render(request, template, context)
