from django.db import models
from django.forms import ValidationError
import re
# Create your models here.

def validator(value):
    if not re.match(r'^[0-9]', value):
        raise ValidationError('invalid type')

class Userinfo(models.Model):
    Pnn = models.IntegerField(primary_key=True, null=False, unique=True)
    u_name = models.CharField(max_length=30)
    pwd = models.CharField(max_length=30)
    # card = models.ForeignKey(
    #     'PersonalCardInfo',
    #     on_delete=models.CASCADE,
    # )
    pcard_Fpcn = models.IntegerField(default=0)

class MetaCardInfo(models.Model):
    ICnn = models.IntegerField(primary_key=True, null=False, unique=True)
    companyNm = models.CharField(max_length=100)
    c_name = models.CharField(max_length=30)

class BalanceCheck(models.Model):
    Bpn = models.IntegerField(primary_key=True, null=False, unique=True,default=0)
    balance = models.IntegerField(default=0)
    mcard_Ficnn = models.IntegerField(default=0)
    pcard_Fpcn = models.IntegerField(default=0)
    puser_Fpun = models.IntegerField(default=0)

class PersonalcardInfo(models.Model):
    Pcn = models.IntegerField(primary_key=True, null=False, unique=True)
    card_name = models.CharField(max_length=30)
    Balance = models.IntegerField(default=0)
    c_num = models.IntegerField(default=0)
    cvc = models.IntegerField(default=0)
    mcard_Ficnn = models.IntegerField(default=0)
    puser_Fpun = models.IntegerField(default=0)
    imgfile = models.ImageField(blank=True)



