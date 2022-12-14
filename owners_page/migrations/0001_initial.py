# Generated by Django 4.1.3 on 2022-11-25 11:01

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CarOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=12, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(12)])),
                ('location', models.CharField(max_length=10)),
                ('wallet', models.IntegerField(default=0)),
                ('car_owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=20)),
                ('car_model', models.CharField(max_length=20)),
                ('car_seats', models.IntegerField()),
                ('gearbox', models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], default='choose gearbox', max_length=50)),
                ('available_car', models.BooleanField(default=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('extra_info', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='owners_page.carowner')),
            ],
        ),
    ]
