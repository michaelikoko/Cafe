# Generated by Django 4.1.3 on 2022-12-02 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_formpage_form_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formpage',
            name='form_image',
        ),
    ]
