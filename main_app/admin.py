from django.contrib import admin
from .models import Cat, CatToy

# Register your models here.

#import models
from .models import Cat

admin.site.register(Cat)
admin.site.register(CatToy)
