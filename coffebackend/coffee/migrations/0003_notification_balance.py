# Generated by Django 5.1.1 on 2024-10-30 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0002_alter_history_orderid_alter_history_productname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='balance',
            field=models.CharField(blank=True, null=True),
        ),
    ]
