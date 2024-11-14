from django.db import models
from django.contrib import admin
class bankloan(models.Model):
      Name=models.CharField(max_length=15)
      accountno=models.IntegerField(primary_key="accountno")
      loan_amount=models.IntegerField()
      salary=models.FloatField()
      Phone_no=models.IntegerField()
class bankloanAdmin(admin.ModelAdmin):
     list_display=('Name','accountno','loan_amount','salary','Phone_no')
