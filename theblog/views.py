from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

def LikeView(request, pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	likes = False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		likes =False
	else:
		post.likes.add(request.user)
		likes = True
	return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	#ordering = ['-id']
	ordering = ['-post_date']

	context_object_name = 'posts'  # Custom context variable for posts

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context


def CategoryListView(request):
	cat_menu_list = Category.objects.all()
	return render(request,'category_list.html', {'cat_menu_list': cat_menu_list})

def CategoryView(request, cats):
	category_posts = Post.objects.filter(category=cats.replace('-', ' '))
	return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts':category_posts})

class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article-details.html'

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
		stuff  = get_object_or_404(Post, id=self.kwargs['pk'])
		total_likes = stuff.total_likes()

		liked = False
		if stuff.likes.filter(id=self.request.user.id).exists():
			liked = True
		context["cat_menu"] = cat_menu
		context["total_likes"] = total_likes
		context["liked"] = liked
		return context

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'
	#fields = '__all__'
	#fields =('title', 'title_tag', 'body')
	def form_valid(self, form):
    # Set the author to the currently logged-in user
		form.instance.author = self.request.user
		return super().form_valid(form)

class AddCategoryView(CreateView):
	model = Category
	template_name ='add_category.html'
	fields = '__all__'

class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'update_post.html'
	#fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')

class AddCommentView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name ='add_comment.html'
	#fields = '__all__'
	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)
success_url = reverse_lazy('home')
