# Generated by Django 3.0.2 on 2020-01-31 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_auto_20200131_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='qrcode',
        ),
        migrations.AddField(
            model_name='ticket',
            name='qrcode',
            field=models.ImageField(blank=True, null=True, upload_to='qrcode'),
        ),
    ]
