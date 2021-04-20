# Generated by Django 3.1.7 on 2021-04-17 09:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meetup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('pic', models.ImageField(default='default.png', upload_to='profile_pics')),
            ],
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='credit_card_number',
            field=models.PositiveBigIntegerField(validators=[django.core.validators.MinValueValidator(1000000000000000), django.core.validators.MaxValueValidator(9999999999999999)]),
        ),
        migrations.RemoveField(
            model_name='event',
            name='attendees',
        ),
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(blank=True, related_name='event_attendees', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='balance',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)]),
        ),
    ]