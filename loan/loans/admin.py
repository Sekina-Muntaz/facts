from django.contrib import admin
from .models import Loan,Interest,Client


admin.site.register(Loan)
admin.site.register(Interest)
admin.site.register(Client)
# Register your models here.

