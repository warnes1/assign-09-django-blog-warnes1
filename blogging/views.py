from django.http.response import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here


# No longer using, temporary use only
# def stub_view(request, *args, **kwargs):
#     body = "Stub View\n\n"
#     if args:
#         body += "Args: \n"
#         body += "\n".join(["\t%s" % a for a in args])
#     if kwargs:
#         body += "Kwargs:\n"
#         body += "\n".join(["\t%s: %s" % b for b in kwargs.items()])
#     return HttpResponse(body, content_type="text/plain")


class PostListView(ListView):
    #    model = Post
    #     context_object_name = 'post_list'
    queryset = Post.objects.order_by("-published_date").exclude(
        published_date__isnull=True
    )
    template_name = "blogging/list.html"


class PostDetailView(DetailView):
    try:
        queryset = Post.objects.exclude(published_date__isnull=True)
        template_name = "blogging/detail.html"
    except Post.DoesNotExist:
        raise Http404
