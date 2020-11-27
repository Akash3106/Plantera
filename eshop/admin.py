from django.contrib import admin

from .models import Product
from .models import relprod

admin.site.register(Product)
admin.site.register(relprod)
