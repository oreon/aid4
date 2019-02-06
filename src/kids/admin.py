from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.
@admin.register(Kid)
class KidAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'date_of_birth', 'gender' , 'sponsor', 'age', 'updated', 'image_tag']
    readonly_fields = ['image_tag', 'age']
    search_fields = ['name', 'city', 'sponsor__email']
    list_filter = ('gender', 'created', )
    #list_filter = ( 'created',  'user')

    def image_tag(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="200" height="200" />'.format(obj.photo.url))

    image_tag.short_description = 'Image'

@admin.register(Sponsorship)
class SponsorshipAdmin(admin.ModelAdmin):   
    list_display = ( 'created', 'action', 'sponsor', 'kid')
    list_filter = ( 'created', )
    pass 

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):   
    pass 