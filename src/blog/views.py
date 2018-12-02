from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import PostModel
from .forms import PostModelForm


# @login_required()
def post_model_create_view(request):
    # if request.method == 'POST':
    #     print(request.POST)
    #     form = PostModelForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit=False)
    #         print(form.cleaned_data)

    form = PostModelForm(request.POST or None)
    context = {
        'form': form
    }

    if form.is_valid():
        obj = form.save(commit=False)
        # print(obj.title)
        obj.save()
        messages.success(request, 'Created a new Blog Post!')
        context = {
            'form': PostModelForm()
        }
        # return HttpResponseRedirect('/blog/{id}'.format(id=obj.id))

    template = 'blog/create-view.html'

    return render(request, template, context)


# @login_required()
def post_model_update_view(request, id=None):
    obj = get_object_or_404(PostModel, id=id)

    form = PostModelForm(request.POST or None, instance=obj)
    context = {
        # 'object': obj,
        'form': form
    }

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, 'Updated Post!')
        return HttpResponseRedirect('/blog/{id}'.format(id=obj.id))

    template = 'blog/update-view.html'
    return render(request, template, context)


def post_model_delete_view(request, id=None):
    obj = get_object_or_404(PostModel, id=id)

    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Post Deleted!')
        return HttpResponseRedirect('/blog/')

    context = {'object': obj}
    template = 'blog/delete-view.html'
    return render(request, template, context)


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


def post_model_robust_view(request, id=None):
    obj = None
    context = {}
    success_message = 'A New Post was Created!'

    if id is None:
        '''OBJ is Could be Created...'''
        template = 'blog/create-view.html'
    else:
        '''OBJ Probally Exists...'''
        obj = get_object_or_404(PostModel, id=id)
        success_message = 'A New Post was Created!'
        context['object'] = obj
        template = 'blog/detail-view.html'
        if 'edit' in request.get_full_path():
            template = 'blog/update-view.html'

        if 'delete' in request.get_full_path():
            template = 'blog/delete-view.html'
            if request.method == 'POST':
                obj.delete()
                messages.success(request, 'Post Deleted!')
                return HttpResponseRedirect('/blog/')

    # if 'edit' in request.get_full_path() or 'create' in request.get_full_path():
        form = PostModelForm(request.POST or None, instance=obj)
        context['form'] = form
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, success_message)
        if obj is not None:
            return HttpResponseRedirect('/blog/{id}'.format(id=id))
        context[form] = PostModelForm()
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
