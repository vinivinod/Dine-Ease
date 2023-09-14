from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, name, phone, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone=phone, 
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name,phone, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            name=name,
            phone=phone,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    CUSTOMER = 1
    EMPLOYEE = 2
    

    ROLE_CHOICE = (
        (CUSTOMER, 'Customer'),
        (EMPLOYEE, 'Employee'),
    )

    username=None
    first_name = None
    last_name = None
    USERNAME_FIELD = 'email'
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=12, blank=True)
    password = models.CharField(max_length=128)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True,default='1')

    # date_joined = models.DateTimeField(auto_now_add=True)
    # last_login = models.DateTimeField(auto_now_add=True)
    # created_date = models.DateTimeField(auto_now_add=True)
    # modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)

    
    REQUIRED_FIELDS = ['name', 'phone']

    objects = UserManager()

    def _str_(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True



class menus(models.Model):
    CATEGORY_CHOICES = (
        ('Kerala', 'Kerala'),
        ('Chineese', 'Chineese'),
        ('North Indian', 'North Indian'),
        ('Arabian', 'Arabian'),
        ('Deserts', 'Deserts'),
        ('Beverages', 'Beverages'),
    )

    SUBMENU_CHOICES = (
        ('Breads', 'Breads'),
        ('Curries', 'Curries'),
        ('Rice Dishes','Rice Dishes'),
        ('Seafoods','Seafoods'),
        ('Deserts','Deserts'),
        ('Appetizers','Appetizers'),
        ('Main Course','Main Course'),
        ('Tandoori delights','Tandoori delights'),
        ('Chaats','Chaats'),
        ('Rolls & Grills','Rolls & Grills'),
        ('Hot Beverage','Hot Beverage'),
        ('Cold Beverage','Cold Beverage'),
    )

    SUB_SUBMENU_CHOICES = (
        ('Vegetarian', 'Vegetarian'),
        ('Non-Vegetarian', 'Non-Vegetarian'),
       
    )

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='')
    submenu = models.CharField(max_length=50, choices=SUBMENU_CHOICES, default='', blank=True)
    sub_submenu = models.CharField(max_length=50, choices=SUB_SUBMENU_CHOICES, default='', blank=True)
    desc = models.CharField(max_length=300)
    price = models.FloatField()
    img = models.ImageField(upload_to='menus/', blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class hmenus(models.Model):
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=300)
    price=models.FloatField()
    img = models.ImageField(upload_to='menus/', blank=True, null=True)

    def __str__(self):
        return self.name

# class Reservation(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length=15)
#     reservation_date = models.DateField()
#     num_of_persons = models.PositiveIntegerField()

#     def __str__(self):
#         return self.name
from django.db import models

class Reservation(models.Model):
    reservation_id = models.CharField(max_length=20, primary_key=True,default=None)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    num_of_persons = models.PositiveIntegerField()
    table_id = models.ForeignKey('home.tables', on_delete=models.CASCADE,default=None)  # Use string reference
    reservation_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.reservation_id


    
class tables(models.Model):
    tab_id = models.CharField(max_length=20, primary_key=True)
    desc = models.CharField(max_length=300)

    def __str__(self):
        return self.tab_id


