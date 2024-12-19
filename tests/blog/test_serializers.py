import pytest
# from posts.models import Posts

# from posts.serializers import PostsSerializer
from blog.serializers import PostsSerializer
from django.conf import settings
from django.urls import reverse

@pytest.mark.django_db
class TestPostsSerializer:
    
    @pytest.fixture
    def post(self, posts_factory):
        # Create a post instance using the posts_factory fixture
        return posts_factory(title="Test Post", content="This is a test content.", status="Published")
    
    def test_posts_serializer_fields(self, post):
        # Test that the serializer correctly serializes the fields
        serializer = PostsSerializer(post)
        data = serializer.data
        
        # Check if the required fields are in the serialized data
        assert 'id' in data
        assert 'title' in data
        assert 'snippet' in data
        assert 'content' in data
        assert 'image' in data
        assert 'status' in data
        assert 'tags' in data
        assert 'created_at' in data
        assert 'publish' in data
        # assert 'read_time' in data
        assert 'slug' in data
        assert 'author' in data
        assert 'author_info' in data
    
    def test_get_read_time(self, post):
        post.content = 'Understanding the Issue: It seems like your application is not correctly handling the authentication state after a browser refresh. Here are some potential causes and solutions: 1. Local Storage Persistence'
       # Check that the 'get_read_time' method in the serializer works
        serializer = PostsSerializer(post)
        read_time = serializer.get_read_time(post)
       
        # Assuming that get_readtime() method returns an integer value, e.g., 5 for the time in minutes
        assert isinstance(read_time, int) 
        assert read_time >= 0 
    
    def test_get_author_info(self, post):
        # Check that 'get_author_info' method works correctly
        serializer = PostsSerializer(post)
        author_info = serializer.get_author_info(post)
        
        # Test the fields in author_info
        assert 'id' in author_info
        assert 'full_name' in author_info
        assert 'profile_picture' in author_info
        
        # Check full name formatting
        assert author_info['full_name'] == f'{post.author.first_name} {post.author.last_name}'
        
        # Test profile picture URL
        if post.author.profile_picture:
            # Check if the full URL is correct
            assert author_info['profile_picture'] == settings.BASE_URL + post.author.profile_picture.url
        else:
            # If there's no profile picture, the URL should be None
            assert author_info['profile_picture'] is None
    
    def test_serialize_post_data(self, post):
        # Test the entire serialization of the post
        serializer = PostsSerializer(post)
        data = serializer.data
        
        # You can check individual fields or make sure that serialized data matches the expected structure
        assert data['title'] == post.title
        assert data['content'] == post.content
        assert data['status'] == post.status
        assert 'author_info' in data