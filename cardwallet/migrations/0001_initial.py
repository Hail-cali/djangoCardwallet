# Generated by Django 3.2 on 2021-05-19 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceCheck',
            fields=[
                ('Bpn', models.IntegerField(default=0, primary_key=True, serialize=False, unique=True)),
                ('balance', models.IntegerField(default=0)),
                ('mcard_Ficnn', models.IntegerField(default=0)),
                ('pcard_Fpcn', models.IntegerField(default=0)),
                ('puser_Fpun', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MetaCardInfo',
            fields=[
                ('ICnn', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('companyNm', models.CharField(max_length=100)),
                ('c_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalcardInfo',
            fields=[
                ('Pcn', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('card_name', models.CharField(max_length=30)),
                ('Balance', models.IntegerField(default=0)),
                ('c_num', models.IntegerField(default=0)),
                ('cvc', models.IntegerField(default=0)),
                ('mcard_Ficnn', models.IntegerField(default=0)),
                ('puser_Fpun', models.IntegerField(default=0)),
                ('imgfile', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('Pnn', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('u_name', models.CharField(max_length=30)),
                ('pwd', models.CharField(max_length=30)),
                ('pcard_Fpcn', models.IntegerField(default=0)),
            ],
        ),
    ]
