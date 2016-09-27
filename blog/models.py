from django.db import models
from datetime import datetime
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.contrib.auth.models import User
import uuid



class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Packages(models.Model):
    user = models.ForeignKey(User)
    package_id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    sender_name = models.CharField(max_length=200, blank=True)
    sender_customer_number = models.CharField(max_length=20, blank=True)
    sender_telephone_number = models.CharField(max_length=15, blank=False)
    sender_email = models.EmailField(max_length=254, blank=True)
    sender_country = models.CharField(max_length=200, blank=False)
    sender_street_name = models.CharField(max_length=200, blank=False)
    sender_street_number = models.PositiveSmallIntegerField(blank=False)
    sender_postal_code = models.CharField(max_length=16, blank=False)
    recipient_name = models.CharField(max_length=200, blank=True)
    recipient_customer_number = models.CharField(max_length=20, blank=True)
    recipient_telephone_number = models.CharField(max_length=15, blank=False)
    recipient_email = models.EmailField(max_length=254, blank=True)
    recipient_country = models.CharField(max_length=200, blank=False)
    recipient_street_name = models.CharField(max_length=200, blank=False)
    recipient_street_number = models.PositiveSmallIntegerField(blank=False)
    recipient_postal_code = models.CharField(max_length=16, blank=False)
    package_height = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    package_width = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    package_length = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    package_weight = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    collect_on_delivery = models.BooleanField(default=False, blank=False)
    collect_on_delivery_amount = models.IntegerField(blank=True, default=0)
    is_package_delivered = models.BooleanField(default=False)
    additional_info = models.TextField(blank=True)
    deliver_till = models.DateTimeField(blank=False)

    def add_package(self):
        self.save()
    def parsing_deliver_till(self):
        self.parsed_deliver_till = parse_datetime(self.deliver_till)

    def __str__(self):
        return self.package_id + " |  FROM:  " + self.sender_name + " |  TO:  " + self.recipient_name
