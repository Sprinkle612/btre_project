# Generated by Django 2.2.5 on 2019-09-29 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20190929_1558'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='messsage',
            new_name='message',
        ),
    ]
