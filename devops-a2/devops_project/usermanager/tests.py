from django.test import TestCase
from django.contrib.auth.models import User
from parameterized import parameterized

# Create your tests here.

class UserManagerTest(TestCase):
    def setUp(self):
        # Admin User
        User.objects.create_superuser(username = 'admin', email = 'admin@django.com', password = 'admin')
        # Super User
        User.objects.create_user(username = 'staff', email = 'staff@django.com', password = 'staff', is_staff = True)
        # Client User
        User.objects.create_user(username = 'guest', email = 'guest@django.com', password = 'guest')
    
    @parameterized.expand([
        ("Test Case 1 - create new user", { "firstname": "Staff", "lastname": "User", "username": "staffuser", "email": "newstaffuser@django.com", "password": "super@123", "confirmpassword":  "super@123" }, "user successfully created"),
        ("Test Case 2 - create new user - without last name", { "firstname": "Steve", "lastname": "", "username": "steve", "email": "steve@django.com", "password": "steve@123", "confirmpassword":  "steve@123" }, "user successfully created"),
        ("Test Case 3 - existing username", { "firstname": "Anna", "lastname": "Steve", "username": "guest", "email": "anna@django.com", "password": "super@123", "confirmpassword":  "super@123" },"user already exists"),
        ("Test Case 4 - existing email", { "firstname": "Ankit", "lastname": "Mahajan", "username": "ankit", "email": "guest@django.com", "password": "super@123", "confirmpassword":  "super@123" },"user successfully created"),
        ("Test Case 5 - password and confirm password doesnot match", { "firstname": "Shruti", "lastname": "Sharma", "username": "staffuser", "email": "newstaffuser@django.com", "password": "super@123", "confirmpassword":  "super@1234" }, "user successfully created"),

    ])
    def test_add_user(self, name, input, expected):
        print("\n", name)
        # Admin login
        self.client.login(username='admin', password='admin')
        session = self.client.session
        session.save()
        # create post data
        post_data = input
        # cal api
        response = self.client.post('/users/add/', post_data, follow=True)
        # match output
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        print("Expected Output ==>", expected)
        print("Actual Output ==>", str(messages[0]))
        self.assertEqual(str(messages[0]), expected)
    
