# Generated by Django 2.2.2 on 2020-03-03 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iiw_book', '0004_sessionstate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendee',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='attendee',
            name='denied',
        ),
        migrations.AddField(
            model_name='attendee',
            name='conference',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='attendee',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='attendee',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
