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
        (CUSTOMER, 'CUSTOMER'),
        (EMPLOYEE, 'EMPLOYEE'),
    )

    username=None
    first_name = None
    last_name = None
    USERNAME_FIELD = 'email'
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=12, blank=True)
    password = models.CharField(max_length=128)
    role = models.IntegerField(choices=ROLE_CHOICE, blank=True, null=True,default='1')

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

    def set_employee_role(self):
        self.role=CustomUser.EMPLOYEE
        self.save()

from django.db import models

class Employee(models.Model):
    position = models.CharField(max_length=100,editable=False,null=True,default='default')  # Field for the employee's position
    years_of_experience = models.PositiveIntegerField(null=True,default='default')  # Field for years of experience
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address = models.TextField(default='',null=True)  # Field for employee's address
    id_proof_number = models.CharField(max_length=100,default='',null=True)  # Field for employee's ID proof number
    education = models.CharField(max_length=100,default='',null=True)  # Field for employee's education
    qualification = models.CharField(max_length=100,default='',null=True)  # Field for employee's qualification
    emergency_name = models.CharField(max_length=100,default='',null=True)  # Field for emergency contact name
    emergency_contact_number = models.CharField(max_length=12,default='',blank=True, null=True)  # Field for emergency contact number
    image = models.ImageField(upload_to='employee_profile/', blank=True, null=True)
    active = models.BooleanField(default=True)
    
    # name = models.CharField(max_length=50)
    # email = models.EmailField(max_length=100, unique=True)
    # phone = models.CharField(max_length=12, blank=True)
    # password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.user.username} - {self.position}"


class menus(models.Model):
    CATEGORY_CHOICES = (
        ('Kerala', 'Kerala'),
        ('Chineese', 'Chineese'),
        ('North Indian', 'North Indian'),
        ('Arabian', 'Arabian'),
        ('Beverages', 'Beverages'),
    )

    SUBMENU_CHOICES = (
        ('Breads', 'Breads'),
        ('Curries', 'Curries'),
        ('Rice Dishes','Rice Dishes'),
        ('Appetizers','Appetizers'),
        ('Main Course','Main Course'),
        ('Breads & Accompaniments', 'Breads & Accompaniments'),
        ('Rolls & Grills','Rolls & Grills'),
        ('Hot Beverage','Hot Beverage'),
        ('Cold Beverage','Cold Beverage'),
    )

    SUB_SUBMENU_CHOICES = (
        ('Vegetarian', 'Vegetarian'),
        ('Non-Vegetarian', 'Non-Vegetarian'),
        ('Water-based','Water-based'),
        ('Milk-based','Milk-based')
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

# from django.db import models

# class Cart(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
#     menu = models.ForeignKey(menus, on_delete=models.CASCADE, null=True)

#     def __str__(self):
#         return f"Cart for {self.user} - {self.menu.name}"


from django.db import models


class AddToCart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    menu = models.ForeignKey(menus, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Cart for {self.user.username} - {self.menu.name} ({str(self.quantity)} items)"


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
    time_slot = models.CharField(max_length=20, null=True, blank=True)  # Add the time_slot field
    table_id = models.ForeignKey('home.tables', on_delete=models.CASCADE,null=True)  # Use string reference
    reservation_date = models.DateField()
    is_active = models.BooleanField(default=True)

    menu_name = models.CharField(max_length=100, null=True, blank=True)
    menu_price = models.FloatField(null=True, blank=True)


    def __str__(self):
        return self.reservation_id


    
class tables(models.Model):
    tab_id = models.CharField(max_length=20, primary_key=True)
    desc = models.CharField(max_length=300)

    def __str__(self):
        return self.tab_id

from django.db import models

class TimeSlot(models.Model):
    slot_id = models.AutoField(primary_key=True)
    slot_time = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.slot_time

    class Meta:
        verbose_name = "Time Slot"
        verbose_name_plural = "Time Slots"

# from django.db import models
# from django.contrib.auth.models import CustomUser
# from home import menus  # Import your Menu model

# class Fav(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     items = models.ManyToManyField(menus)  # Assuming Menu is the model for products

from django.db import models

class BillingInformation(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)  # Use a one-to-one relationship with the User model
    address = models.TextField()
    town = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username  # Return a meaningful representation for the model

    def get_full_address(self):
        return f"{self.address}, {self.city}, {self.zip_code}"
