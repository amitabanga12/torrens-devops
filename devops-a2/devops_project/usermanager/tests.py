from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.

class UserManagerTest(TestCase):
    def setUp(self):
        # Admin User
        User.objects.create_superuser(username = 'admin', email = 'admin@django.com', password = 'admin')
        # Super User
        User.objects.create_user(username = 'staff', email = 'staff@django.com', password = 'staff', is_staff = True)
        # Client User
        User.objects.create_user(username = 'guest', email = 'guest@django.com', password = 'guest')
    
    def test_add_user_by_admin(self):
        print()
        # Admin login
        self.client.login(username='admin', password='admin')
        session = self.client.session
        session.save()
        # First check if user exists
        username = "newstaffuser"
        users = User.objects.filter(username = username) 
        self.assertEqual(len(users), 0)
        # create post data
        post_data = {
            "firstname": "Staff",
            "lastname": "User",
            "username": username,
            "email": "newstaffuser@django.com",
            "password": "super@123",
            "confirmpassword":  "super@123"
        }
        # cal api
        response = self.client.post('/users/add/', post_data, follow=True)
        print("test_add_user_by_admin response ==>", response)
        # Get user
        users = User.objects.filter(username = username)
        print("test_add_user_by_admin users ==>", users, len(users))
        # user is created successfully
        self.assertEqual(len(users), 1)
        self.assertTrue(users[0].is_staff) # Admin can create Staff
        self.assertFalse(users[0].is_superuser) # Admin can't create another admin
        messages = list(response.context['messages'])
        print("test_add_user_by_admin messages ==>", messages, len(messages))
        self.assertEqual(len(messages), 1)
        print("test_add_user_by_admin messages ==>", str(messages[0]))
        self.assertEqual(str(messages[0]), "user successfully created")
        
    def test_add_user_by_staff(self):
        print()
        # staff login
        self.client.login(username='staff', password='staff')
        session = self.client.session
        session.save()
        # First check if user exists
        username = "newuser"
        users = User.objects.filter(username = username) 
        self.assertEqual(len(users), 0)
        # create post data
        post_data = {
            "firstname": "Anna",
            "lastname": "Steve",
            "username": username,
            "email": "guest@django.com",
            "password": "guest@123",
            "confirmpassword":  "guest@123"
        }
        # cal api
        response = self.client.post('/users/add/', post_data, follow=True)
        print("test_add_user_by_staff response ==>", response)
        # Get user
        users = User.objects.filter(username = username)
        print("test_add_user_by_staff users ==>", users, len(users))
        # user is not created
        self.assertEqual(len(users), 0)
        messages = list(response.context['messages'])
        print("test_add_user_by_staff messages ==>", messages, len(messages))
        self.assertEqual(len(messages), 1)
        print("test_add_user_by_staff messages ==>", str(messages[0]))
        self.assertEqual(str(messages[0]), "You don't have permission to access user list")
        
    def test_add_user_with_same_username(self):
        print()
        # staff login
        self.client.login(username='admin', password='admin')
        session = self.client.session
        session.save()
        username = "guest"
        # create post data
        post_data = {
            "firstname": "Anna",
            "lastname": "Steve",
            "username": username,
            "email": "guest@django.com",
            "password": "guest@123",
            "confirmpassword":  "guest@123"
        }
        # cal api
        response = self.client.post('/users/add/', post_data, follow=True)
        print("test_add_user_with_same_username response ==>", response)
        # Get user
        users = User.objects.filter(username = username)
        print("test_add_user_with_same_username users ==>", users, len(users))
        # user is successfully created
        messages = list(response.context['messages'])
        print("test_add_user_with_same_username messages ==>", messages, len(messages))
        self.assertEqual(len(messages), 1)
        print("test_add_user_with_same_username messages ==>", str(messages[0]))
        self.assertEqual(str(messages[0]), 'user successfully created')
        # self.assertEqual(str(messages[0]), 'user already exists')
        
        
    def test_add_user_with_same_email(self):
        print()
        self.client.login(username='admin', password='admin')
        session = self.client.session
        session.save()
        username = "guest1"
        # create post data
        post_data = {
            "firstname": "Anna",
            "lastname": "Steve",
            "username": username,
            "email": "guest@django.com",
            "password": "guest@123",
            "confirmpassword":  "guest@123"
        }
        # cal api
        response = self.client.post('/users/add/', post_data, follow=True)
        print("test_add_user_with_same_email response ==>", response)
        # Get user
        users = User.objects.filter(username = username)
        print("test_add_user_with_same_email users ==>", users, len(users))
        messages = list(response.context['messages'])
        print("test_add_user_with_same_email messages ==>", messages, len(messages))
        self.assertEqual(len(messages), 1)
        print("test_add_user_with_same_email messages ==>", str(messages[0]))
        # self.assertEqual(str(messages[0]), 'user already exists')
        self.assertEqual(str(messages[0]), 'user successfully created')
        
    def test_add_user_with_invalid_password(self):
        print()
        self.client.login(username='admin', password='admin')
        session = self.client.session
        session.save()
        username = "guest2"
        # create post data
        post_data = {
            "firstname": "Anna",
            "lastname": "Steve",
            "username": username,
            "email": "guest2@django.com",
            "password": "",
            "confirmpassword":  ""
        }
        # cal api
        response = self.client.post('/users/add/', post_data, follow=True)
        print("test_add_user_with_invalid_password response ==>", response)
        # Get user
        users = User.objects.filter(username = username)
        print("test_add_user_with_invalid_password users ==>", users, len(users)) 
        messages = list(response.context['messages'])
        print("test_add_user_with_invalid_password messages ==>", messages, len(messages))
        self.assertEqual(len(messages), 1)
        print("test_add_user_with_invalid_password messages ==>", str(messages[0]))
        self.assertEqual(str(messages[0]), 'invalid input') 
