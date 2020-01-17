# Generated by Django 2.2.9 on 2020-01-14 09:37

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20200114_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='carousel_image_information',
            field=wagtail.core.fields.RichTextField(blank=True, default='Carousel Image Information', null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='carousel_image_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]