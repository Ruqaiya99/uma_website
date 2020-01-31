# Generated by Django 2.2.9 on 2020-01-31 05:50

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('background', wagtail.core.fields.RichTextField(null=True)),
                ('history', wagtail.core.fields.RichTextField(null=True)),
                ('participate', wagtail.core.fields.RichTextField(null=True)),
                ('participate_points', wagtail.core.fields.StreamField([('text', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(blank=False, max_length=255, null=True, required=True))]))], blank=True, null=True)),
            ],
            options={
                'verbose_name': 'About Us Page',
            },
            bases=('wagtailcore.page',),
        ),
    ]