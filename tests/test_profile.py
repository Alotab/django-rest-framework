import pytest
from profile.models import User

@pytest.mark.django_db
def test_user_create():
    User.objects.create(username='pytesteztss', email='tez@elon.com', password='Alaska020')
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_user_count():
    count = User.objects.all().count()
    print(count) # should print 0 because the database here doesn't persist data
    assert count == 0



def test_set_check_username(user_1):
    print('check username')
    assert user_1.username == 'test1'

def test_set_check_password(user_1):
    print('check password')
    user_1.set_password('Alaska020')
    assert user_1.check_password('Alaska020') is True


## using the user factory in conftest.py
# def test_new_user(new_user1):
#     assert new_user1.first_name == 'MyTestName'

# def test_new_user(new_user2):
#     assert new_user2.is_staff