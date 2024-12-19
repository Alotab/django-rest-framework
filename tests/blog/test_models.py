import pytest 
from django.urls import reverse

pytestmark = pytest.mark.django_db


class TestPostsModel:
    def test_str_return(self, posts_factory):
        post = posts_factory(title='test-post')
        assert post.__str__() == 'test-post'

    def test_slug_return(self, posts_factory):
        post = posts_factory(title='test post')
        post.create_slug(None, post)
        assert post.slug == 'test-post'

    def test_get_absolute_url(self, posts_factory):
        post = posts_factory.create(title='Test Post for URL', slug='test-post-for-url')
        url = post.get_absolute_url()
        expected_url = reverse('blog:post_detail', kwargs={'slug': post.slug, 'pk': post.id})
        assert url == expected_url



# Explicitly test the slug method in the Post Model
@pytest.mark.django_db
def test_create_slug_method(posts_factory):
    post = posts_factory.create(title='Test Post for Slug')
    
    # Call the create_slug method manually
    post.create_slug(None, post)  
    assert post.slug == 'test-post-for-slug'