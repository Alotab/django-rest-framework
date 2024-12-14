from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
# from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib import messages
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.views.generic import UpdateView
from .models import Comment, Posts
from django.views.decorators.csrf import csrf_exempt
# from users.models import CustomUser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from taggit.models import Tag
from .forms import PostForm
from .utilss import get_real_time_date_format
from rest_framework.viewsets import ModelViewSet
from django.views.generic.list import ListView
from .serializers import PostsSerializer, PostCreateSerializer



## REACT URLS VIEWS
class PostViewSet(ModelViewSet):
    queryset = Posts.objects.all()
    # serializer_class = PostsSerializer


    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostsSerializer
        return PostCreateSerializer

        # if self.action == 'create':
        #     return 
        # return 

    def get_queryset(self):  

        # Customize queryset if needed
        return Posts.objects.filter(status="Published")
    
    def get_object(self):
        # Customize object retrieval logic if needed
        return super().get_object()
    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

    def perform_create(self, serializer):
        # Customize object creation logic
        post = serializer.save()
        post.author = self.request.user
        post.save()




@api_view(['POST'])
def create_posts(request):
    if request.method == 'POST':
        serializer = PostsSerializer(data=request.data)
        if serializer.is_valid():
            # You can save the data to the database if necessary
            # For example, saving it to a model
            posts = Posts.objects.create(
                title=serializer.validated_data['title'],
                snippet=serializer.validated_data['snippet'],
                tags=serializer.validated_data['tags'],
                content=serializer.validated_data['content'],
                image=serializer.validated_data.get('image'),
                status=serializer.validated_data['status'],
            )
            return Response({'status': 'Post created successfully', 'posts': serializer.data})
        return Response(serializer.errors, status=400)


# class PostsView(ListView):
#   model = Posts
#   paginate_by = 3
#   context_object_name = 'posts'
#   template_name = 'blog/home.html'
#   ordering = ['publish']
  





## UPDATE THE VIEW TO RECIEVE DATA FROM REACT 
@csrf_exempt  # If you are not using CSRF tokens, you may need this decorator
def post_blog(request):
    if request.method == 'POST':
        # Create a PostForm instance using request.FILES (for handling image uploads)
        form = PostForm(request.POST, request.FILES)
        
        # Check if form data is valid
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user  # Set the author to the current logged-in user
            post.save()
            
            # Send success response back to the frontend
            response_data = {
                'status': 'success',
                'message': 'Post created successfully!',
                'post': {
                    'title': post.title,
                    'content': post.content,
                    'image': post.image.url if post.image else None,  # Return the image URL
                }
            }
            return JsonResponse(response_data, status=201)  # 201 for resource created
        
        else:
            # If form validation fails, send error message back
            response_data = {'status': 'error', 'message': form.errors}
            return JsonResponse(response_data, status=400)
    
    else:
        # If the request method is not POST, return the empty form
        form = PostForm()
    return render(request, 'blog/createPost.html', {'form': form})



### Works fine just want to update a new one to recieve data from React
# def post_blog(request):
#   if request.method == 'POST':
#     form = PostForm(request.POST, request.FILES)
#     if form.is_valid():
#       post = form.save(commit=False)
#       post.author = request.user
#       # context['meta'] = post.as_meta()
#       post.save()
#       messages.success(request, 'Post created successfully')
#       return redirect('blog:home')
      
#   else:
#     form = PostForm()
#   return render(request, 'blog/createPost.html', {'form': form})




def post_list(request):
    """ List the all the post in the home page """
    posts = Posts.objects.all()
    # posts = Posts.publish.order_by('-publish')
    # post_list = list(posts)
    # trending_post = Post.published.all().order_by('-publish')[:6]
    #   latest_post = Post.published.all().order_by('-publish')[:3]
    tags = Tag.objects.all()

    context = {
    'posts': posts,
    # 'trending_post': trending_post,
    'tags': tags,
    }

    return render(request, 'blog/home.html', context)



def post_detail(request, slug, pk):
    post = get_object_or_404(Posts, slug=slug, id=pk)
    comments = Comment.objects.filter(blog=post)
    # post_tags = post.tags.all()
    # trending_posts = Posts.published.all().order_by('-publish')[:4]
    # post_tags_id = post.tags.values_list('id', flat=True)
    # related_posts = Posts.published.filter(tags__in=post_tags_id).exclude(id=post.id)
    # related_posts = related_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]

    # get the image 
    image =  post.image

    # get the absolute url
    post_image = request.build_absolute_uri(image.url)

    if request.method == 'POST':

      comment = Comment(
        user_comment=request.user,
        comment=request.POST['comment'],
        blog=post,
      )
      comment.save()

      # return redirect('/')
      return HttpResponseRedirect(request.META['HTTP_REFERER'])
  
  

    context = {
    'post': post,
    'comments': comments,
    # 'post_tags': post_tags,
    # 'related_posts': related_posts,
    # 'trending_posts': trending_posts,
    'post_image': post_image,
    }
    return render(request, 'blog/post_detail.html', context)



# class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#   model = Post
#   fields= ['Title', 'content', 'image']

#   def form_valid(self, form):
#     form.instance.author = self.request.user
#     return super().form_valid(form)
  
#   def test_func(self):
#     post = self.get_object()
#     if self.request.user == post.author:
#       return True
#     return False


def post_update(request, slug, pk):
    # post = Post.objects.get(id=pk)
    post = get_object_or_404(Post, slug=slug, id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
      form = PostForm(request.POST, instance=post)
      if form.is_valid():
        form.save()
        return redirect('blog:home')
    
    return render(request, 'blog/createPost.html', {'post': post, 'form': form})



def post_delete(request, slug,  pk):
    post = get_object_or_404(Post, slug=slug, id=pk)
    post.delete()
    return redirect('blog:home')
