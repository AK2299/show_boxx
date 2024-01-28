# Generated by Django 4.2.1 on 2023-06-21 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('others', 'others')], max_length=10, null=True),
        ),
    ]
