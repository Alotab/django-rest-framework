import factory
import pytest
import random
from profile.models import User
from blog.models import Posts

def generate_unique_email():
    return f'fact{random.randint(1000, 9999)}@lom.com'

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = 'fact1'
    password = 'fact10202'
    email = factory.LazyFunction(generate_unique_email)
    is_superuser = True
    is_staff = True


class PostsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Posts
    
    title = 'x'
    snippet = 'x'
    content = 'xx'
    slug = 'x'
    author = factory.SubFactory(UserFactory)
    status = 'published'