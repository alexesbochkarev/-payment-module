# Generated by Django 4.1.6 on 2023-02-08 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='description',
        ),
    ]