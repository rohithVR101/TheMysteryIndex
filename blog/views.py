from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment, Categories, Subscribers
from .forms import PostForm, CommentForm
from random import randint
from django.utils import timezone
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def IndexView(request):
        count = Post.objects.all().count()
        rnd = "post/" + str(randint(1,count))
        if request.method == 'POST':
            if request.POST.get('EMAIL'):
                new=Subscribers()
                new.mailid= request.POST.get('EMAIL')
                new.save()
                return render(request, 'blog/index.html',{'rnd':rnd})
        else:
                return render(request,'blog/index.html',{'rnd':rnd})

class AboutView(TemplateView):
    template_name = 'blog/about.html'

class PostListView(ListView):
    model = Post

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['title'] = "ALL POSTS"
        context['img']="media/headers/main.jpg"
        return context

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post


class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_draft_list.html'

    model = Post

    def get_context_data(self,**kwargs):
            context  = super().get_context_data(**kwargs)
            context['title'] = "DRAFTS"
            context['img']="media/headers/dr.jpg"
            return context

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True,author=self.request.user.id).order_by('create_date')


# CATEGORIES

class MysteriousListView(ListView):
    redirect_field_name = 'blog/post_list.html'

    model = Post

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['title'] = "Mysterious Places"
        context['img']="media/headers/myspl.jpg"
        return context

    def get_queryset(self):
        criterion1 = Q(published_date__isnull=True)
        criterion2 = Q(published_date__isnull=False)
        criterion3 = Q(author=self.request.user.id)
        return Post.objects.filter(category__name='Mysterious Places').filter((criterion3 & criterion1) | (criterion2)).order_by('create_date')

class AncientListView(ListView):
    redirect_field_name = 'blog/post_list.html'

    model = Post

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['title'] = "Ancient Cities"
        context['img']="media/headers/anpl.jpg"
        return context

    def get_queryset(self):
        criterion1 = Q(published_date__isnull=True)
        criterion2 = Q(published_date__isnull=False)
        criterion3 = Q(author=self.request.user.id)
        return Post.objects.filter(category__name='Ancient Cities').filter((criterion3 & criterion1) | (criterion2)).order_by('create_date')

class LegendaryListView(ListView):
    redirect_field_name = 'blog/post_list.html'

    model = Post

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['title'] = "Legendary Places"
        context['img']="media/headers/leg.jpg"
        return context

    def get_queryset(self):
        criterion1 = Q(published_date__isnull=True)
        criterion2 = Q(published_date__isnull=False)
        criterion3 = Q(author=self.request.user.id)
        return Post.objects.filter(category__name='Legendary Places').filter((criterion3 & criterion1) | (criterion2)).order_by('create_date')

class UninhabitedListView(ListView):
    redirect_field_name = 'blog/post_list.html'

    model = Post

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['title'] = "Uninhabited Islands"
        context['img']="media/headers/unhis.jpg"
        return context

    def get_queryset(self):
        criterion1 = Q(published_date__isnull=True)
        criterion2 = Q(published_date__isnull=False)
        criterion3 = Q(author=self.request.user.id)
        return Post.objects.filter(category__name='Uninhabited Islands').filter((criterion3 & criterion1) | (criterion2)).order_by('create_date')

class BizzareListView(ListView):
    redirect_field_name = 'blog/post_list.html'

    model = Post

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['title'] = "Bizzare People"
        context['img']="media/headers/bipe.jpg"
        return context

    def get_queryset(self):
        criterion1 = Q(published_date__isnull=True)
        criterion2 = Q(published_date__isnull=False)
        criterion3 = Q(author=self.request.user.id)
        return Post.objects.filter(category__name='Bizzare People').filter((criterion3 & criterion1) | (criterion2)).order_by('create_date')

class MurdersListView(ListView):
    redirect_field_name = 'blog/post_list.html'

    model = Post

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['title'] = "Murders"
        context['img']="media/headers/mur.jpeg"
        return context

    def get_queryset(self):
        criterion1 = Q(published_date__isnull=True)
        criterion2 = Q(published_date__isnull=False)
        criterion3 = Q(author=self.request.user.id)
        return Post.objects.filter(category__name='Murders').filter((criterion3 & criterion1) | (criterion2)).order_by('create_date')

class SerialListView(ListView):
    redirect_field_name = 'blog/post_list.html'

    model = Post

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['title'] = "Serial Killers"
        context['img']="media/headers/sekil.jpg"
        return context

    def get_queryset(self):
        criterion1 = Q(published_date__isnull=True)
        criterion2 = Q(published_date__isnull=False)
        criterion3 = Q(author=self.request.user.id)
        return Post.objects.filter(category__name='Serial Killers').filter((criterion3 & criterion1) | (criterion2)).order_by('create_date')

class UnexplainedListView(ListView):
    redirect_field_name = 'blog/post_list.html'

    model = Post

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['title'] = "Unexplained Disappearances"
        context['img']="media/headers/undi.jpeg"
        return context

    def get_queryset(self):
        criterion1 = Q(published_date__isnull=True)
        criterion2 = Q(published_date__isnull=False)
        criterion3 = Q(author=self.request.user.id)
        return Post.objects.filter(category__name='Unexplained Disappearances').filter((criterion3 & criterion1) | (criterion2)).order_by('create_date')

class StatuesListView(ListView):
    redirect_field_name = 'blog/post_list.html'

    model = Post

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['title'] = "Stones and Statues"
        context['img']="media/headers/stst.jpg"
        return context

    def get_queryset(self):
        criterion1 = Q(published_date__isnull=True)
        criterion2 = Q(published_date__isnull=False)
        criterion3 = Q(author=self.request.user.id)
        return Post.objects.filter(category__name='Stones and Statues').filter((criterion3 & criterion1) | (criterion2)).order_by('create_date')

class TreasuresListView(ListView):
    redirect_field_name = 'blog/post_list.html'

    model = Post

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['title'] = "Treasures"
        context['img']="media/headers/tr.jpg"
        return context

    def get_queryset(self):
        criterion1 = Q(published_date__isnull=True)
        criterion2 = Q(published_date__isnull=False)
        criterion3 = Q(author=self.request.user.id)
        return Post.objects.filter(category__name='Treasures').filter((criterion3 & criterion1) | (criterion2)).order_by('create_date')

class ShipwrecksListView(ListView):
    redirect_field_name = 'blog/post_list.html'

    model = Post

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['title'] = "Shipwrecks"
        context['img']="media/headers/ship.jpg"
        return context

    def get_queryset(self):
        criterion1 = Q(published_date__isnull=True)
        criterion2 = Q(published_date__isnull=False)
        criterion3 = Q(author=self.request.user.id)
        return Post.objects.filter(category__name='Shipwrecks').filter((criterion3 & criterion1) | (criterion2)).order_by('create_date')

class ETListView(ListView):
    redirect_field_name = 'blog/post_list.html'

    model = Post

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['title'] = "Extra-Terrestrial"
        context['img']="media/headers/et.jpg"
        return context

    def get_queryset(self):
        criterion1 = Q(published_date__isnull=True)
        criterion2 = Q(published_date__isnull=False)
        criterion3 = Q(author=self.request.user.id)
        return Post.objects.filter(category__name='Extra-Terrestrial').filter((criterion3 & criterion1) | (criterion2)).order_by('create_date')

class MonstersListView(ListView):
    redirect_field_name = 'blog/post_list.html'

    model = Post

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['title'] = "Monsters"
        context['img']="media/headers/mon.jpg"
        return context

    def get_queryset(self):
        criterion1 = Q(published_date__isnull=True)
        criterion2 = Q(published_date__isnull=False)
        criterion3 = Q(author=self.request.user.id)
        return Post.objects.filter(category__name='Monsters').filter((criterion3 & criterion1) | (criterion2)).order_by('create_date')

class GhostsListView(ListView):
    redirect_field_name = 'blog/post_list.html'

    model = Post

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['title'] = "Ghosts"
        context['img']="media/headers/ghos.jpg"
        return context

    def get_queryset(self):
        criterion1 = Q(published_date__isnull=True)
        criterion2 = Q(published_date__isnull=False)
        criterion3 = Q(author=self.request.user.id)
        return Post.objects.filter(category__name='Ghosts').filter((criterion3 & criterion1) | (criterion2)).order_by('create_date')

class IncidentsListView(ListView):
    redirect_field_name = 'blog/post_list.html'

    model = Post

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['title'] = "Incidents"
        context['img']="media/headers/inc.jpg"
        return context

    def get_queryset(self):
        criterion1 = Q(published_date__isnull=True)
        criterion2 = Q(published_date__isnull=False)
        criterion3 = Q(author=self.request.user.id)
        return Post.objects.filter(category__name='Incidents').filter((criterion3 & criterion1) | (criterion2)).order_by('create_date')

class EgyptianListView(ListView):
    redirect_field_name = 'blog/post_list.html'

    model = Post

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['title'] = "Egyptian Mysteries"
        context['img']="media/headers/egy.jpg"
        return context

    def get_queryset(self):
        criterion1 = Q(published_date__isnull=True)
        criterion2 = Q(published_date__isnull=False)
        criterion3 = Q(author=self.request.user.id)
        return Post.objects.filter(category__name='Egyptian Mysteries').filter((criterion3 & criterion1) | (criterion2)).order_by('create_date')


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)
