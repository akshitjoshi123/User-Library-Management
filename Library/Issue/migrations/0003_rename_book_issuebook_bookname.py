# Generated by Django 3.2.5 on 2021-07-16 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Issue', '0002_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issuebook',
            old_name='book',
            new_name='bookname',
        ),
    ]
