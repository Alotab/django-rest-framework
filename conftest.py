import pytest
from profile.models import User
from rest_framework.test import APIClient
from pytest_factoryboy import register
from tests.factories import PostsFactory


# register the factory, so we can use through out our tests
register(PostsFactory) 

@pytest.fixture()
def user_1(db):
    user = User.objects.create_user('test1')
    return user


@pytest.fixture()
def new_user_factory(db):
    def create_app_user(
        username: str,
        password: str,
        first_name: str = 'first_name',
        last_name: str = 'last_name',
        email: str = 'testuser@test.com',
        is_staff: str = False,
        is_superuser: str = False,
        is_active: str = False,
    ):
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_active=is_active,
            is_superuser=is_superuser
        )
        return user
    return create_app_user


@pytest.fixture
def new_user1(db, new_user_factory):
    return new_user_factory(username='Tests_user', password='password', first_name='MyTestName')

@pytest.fixture
def new_user2(db, new_user_factory):
    return new_user_factory(username='Tests_user', password='password', first_name='MyTestName', is_staff='True')



# Testing our API endpoints in Rest Framework
@pytest.fixture
def api_client():
    return APIClient