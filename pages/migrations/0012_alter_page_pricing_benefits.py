# Generated by Django 5.1.4 on 2025-05-09 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_faq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='pricing_benefits',
            field=models.TextField(default='Functional Website Template\n        Responsive Web Design\n        Fully Working Contact Form\n        Django Admin Panel\n        Easy Customization – Under 20 Minutes'),
        ),
    ]
