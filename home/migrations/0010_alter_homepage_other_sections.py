# Generated by Django 4.1.3 on 2022-12-02 22:41

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_homepage_other_sections'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='other_sections',
            field=wagtail.fields.StreamField([('sections', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('body', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=100, required=True)), ('text', wagtail.blocks.CharBlock(required=True))])))])))], blank=True, use_json_field=True),
        ),
    ]
