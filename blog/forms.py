from django import forms
from .models import Post, Comment, Packages
from django.utils import timezone as django_tz
from django.contrib.admin import widgets
import datetime
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text',]

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['author', 'text',]

class PackageForm(forms.ModelForm):

    class Meta:
        model = Packages
        widgets = {
            # 'deliver_till': forms.DateTimeInput(attrs={'type':'datetime-local', 'format':'%Y-%m-%d %H:%M'})
            'deliver_till': forms.DateTimeInput(attrs={'type':'datetime-local'}, format=None)
        }
        fields = [
        'package_id',
        'sender_name',
        'sender_customer_number',
        'sender_telephone_number',
        'sender_email',
        'sender_country',
        'sender_street_name',
        'sender_street_number',
        'sender_postal_code',
        'recipient_name',
        'recipient_customer_number',
        'recipient_telephone_number',
        'recipient_email',
        'recipient_country',
        'recipient_street_name',
        'recipient_street_number',
        'recipient_postal_code',
        'package_height',
        'package_width',
        'package_length',
        'package_weight',
        'collect_on_delivery',
        'collect_on_delivery_amount',
        'is_package_delivered',
        'additional_info',
        'deliver_till',]
