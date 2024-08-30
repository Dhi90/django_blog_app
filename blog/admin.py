from django.contrib import admin
from .models import blog,categories,AboutUs

# Register your models here.
class postadmin(admin.ModelAdmin):
    search_fields=('title','content')
    list_filter=('category','created_at')



admin.site.register(blog,postadmin)
admin.site.register(categories)
admin.site.register(AboutUs)
