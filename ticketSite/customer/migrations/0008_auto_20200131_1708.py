# Generated by Django 3.0.2 on 2020-01-31 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_ticket_qrcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='qrcode',
        ),
        migrations.AddField(
            model_name='order',
            name='qrcode',
            field=models.ImageField(blank=True, null=True, upload_to='qrcode'),
        ),
    ]
