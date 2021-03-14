from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import uuid
from django.contrib.auth.models import User

# from django.contrib.auth import get_user_model

# Create your models here.


class Location(models.Model):
    # seller_id = models.CharField(max_length=50, null=True, blank=True)
    # deliveries_id = models.CharField(max_length=50, null=True, blank=True)
    latitude = models.DecimalField(
        max_digits=22, decimal_places=16, blank=True, null=True)
    longitude = models.DecimalField(
        max_digits=22, decimal_places=16, blank=True, null=True)
    address_num = models.IntegerField(null=True, blank=True)
    address1 = models.CharField(max_length=50, null=True, blank=True)
    street = models.CharField(max_length=50, null=True, blank=True)
    area = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    zip = models.CharField(max_length=10, null=True, blank=True)
    # location_id = models.UUIDField(
    #     primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"address: {self.address1}"


class UserType(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Date_Created"))
    updated_at = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=20, unique=True)

    class Meta:
        abstract = True


class Buyer(UserType):
    VERTICAL = (
        ('farming', 'farming'),
        ('insurance', 'insurance'),

    )
    # buyer_id = models.UUIDField(
    #     primary_key=True, default=uuid.uuid4, editable=False)

    vertical = models.CharField(
        max_length=50, default='farming', choices=VERTICAL)
    location_id = models.ForeignKey(
        Location, db_column='location_id', related_name='buyer_location', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Delivery(models.Model):
    STATUS = (
        ('inactive', 'inactive'),
        ('inprogress', 'inprogress'),
        ('delivered', 'delivered'),
        ('abandoned', 'abandoned'),
    )
    # delivery_id = models.UUIDField(
    #     primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField(max_length=50, null=True, blank=True)
    reg_no = models.UUIDField(
        unique=True, default=uuid.uuid4)
    price_kg = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    price_km = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    tax = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    status = models.CharField(
        max_length=15, default='inactive', choices=STATUS)
    location_id = models.ForeignKey(
        Location, db_column='location_id', related_name='transport_location', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Deliveries'

    def __str__(self):
        return f'{self.company_name}'


class Escrow(models.Model):

    PAYMENT = (
        ('PayTM', 'PayTM'),
        ('Credit Card', 'Credit Card'),
        ('Debit Card', 'Debit Card'),
        ('PayPal', 'PayPal')
    )

    STATUS = (
        ('inactive', 'inactive'),
        ('inprogress', 'inprogress'),
        ('failed', 'failed'),
        ('completed', 'completed'),
    )
    # escrow_id = models.UUIDField(
    #     primary_key=True, default=uuid.uuid4, editable=False)
    iban = models.CharField(max_length=50, null=True, blank=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    payment_type = models.CharField(
        max_length=20, default='PayTM', choices=PAYMENT)
    ifsc = models.CharField(max_length=50, default=uuid.uuid4)
    auth_id = models.CharField(max_length=50, default=uuid.uuid4)
    status = models.CharField(
        max_length=20, default='inactive', choices=STATUS)
    # order_id = models.CharField(max_length=50, null=True, blank=True)
    acc_no = models.CharField(
        unique=True, max_length=50, null=True, blank=True)
    # seller_id = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Product(models.Model):

    # class ProductObjects(models.Manager):
    #     def get_queryset(self):
    #         return super().get_queryset().filter(name)

    CATEGORY = (
        ('Food', 'Food'),
        ('Cash', 'Cash'),
        ('Plantation', 'Plantation'),
        ('Horticulture', 'Horticulture')
    )
    CROPS = (
        ('rice', 'rice'),
        ('wheat', 'wheat'),
        ('millets', 'millets'),
        ('pulses', 'pulses'),
        ('oil', 'oil'),
        ('seeds', 'seeds'),
        ('cotton', 'cotton'),
        ('jute', 'jute'),
    )
    # product_id = models.UUIDField(
    #     unique=True, default=uuid.uuid4, editable=False)
    unit_price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    category = models.CharField(
        max_length=30, choices=CATEGORY, default='Food', verbose_name=_("Crop_Category"))
    name = models.CharField(max_length=20, choices=CROPS,
                            default='rice', verbose_name=_("Crop"))
    variety = models.CharField(max_length=15, null=True, blank=True)
    avail_weight = models.SmallIntegerField(null=True, blank=True)
    quantity = models.SmallIntegerField(null=True, blank=True)
    in_stock = models.BooleanField(default=True)
    # is_active = models.BooleanField(default=True)
    # seller_id = models.ForeignKey(
    #     Seller, db_column='seller_id', null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ('unit_price',)

    def __str__(self):
        return f"{self.name} variety: {self.variety} price:{self.avail_weight * self.unit_price}"


class Land(models.Model):
    # land_id = models.UUIDField(
    #     primary_key=True, default=uuid.uuid4, editable=False)
    size = models.SmallIntegerField(null=True, blank=True)
    soil_desc = models.CharField(max_length=200, null=True, blank=True)
    photo_url = models.URLField(max_length=200, null=True, blank=True)
    location_id = models.ForeignKey(
        Location, db_column='location_id', related_name='seller_location', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.size}"


class Seller(UserType):
    owner = models.ForeignKey(
        User, related_name='owner', on_delete=models.CASCADE, null=True)
    # order_id = models.UUIDField(default=uuid.uuid4)

    # location_id = models.CharField(max_length=50, null=True, blank=True)
    land_id = models.ForeignKey(
        Land, db_column='land_id', related_name='land', null=True, on_delete=models.CASCADE)
    product_id = models.ForeignKey(
        Product, db_column='product_id', related_name='seller', null=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(
        default=True, verbose_name=_("Active_Status"))

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.created_at} signed-up:{self.is_active}"


class Order(models.Model):
    STATUS = (
        ('inactive', 'inactive'),
        ('inprogress', 'inprogress'),
        ('delivered', 'delivered'),
        ('abandoned', 'abandoned'),
    )
    # order_id = models.UUIDField(
    #     primary_key=True, default=uuid.uuid4, editable=False)
    buyer_id = models.ForeignKey(
        Buyer, db_column='buyer_id', related_name='buyer_order', null=True, on_delete=models.SET_NULL)
    product_id = models.ForeignKey(
        Product, db_column='product_id', related_name='product_order', null=True, on_delete=models.SET_NULL)
    seller_id = models.ForeignKey(
        Seller, db_column='seller_id', related_name='seller_order', null=True, on_delete=models.SET_NULL)
    # payment_id = models.UUIDField(
    #     default=uuid.uuid4, editable=False, unique=True)
    payment_id = models.ForeignKey(
        Escrow, db_column='payment_id', related_name='payment_order', null=True, on_delete=models.SET_NULL)
    tax = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    order_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    total_price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    paid = models.BooleanField(default=False)
    reqd_date = models.DateField(null=True, blank=True)
    reqd_weight = models.SmallIntegerField(null=True, blank=True)
    quantity = models.SmallIntegerField(null=True, blank=True)
    delivery_pickup = models.BooleanField(default=False)
    reg_no = models.ForeignKey(
        Delivery, db_column='reg_no', related_name='reg_order', null=True, on_delete=models.SET_NULL)
    status = models.CharField(
        max_length=15, default='inactive', choices=STATUS)
    distance = models.SmallIntegerField(null=True, blank=True)
    # location_id = models.ForeignKey(
    #     Location, db_column='location_id', related_name='location order', null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ('reqd_date',)
