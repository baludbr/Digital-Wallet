# Generated by Django 4.1.7 on 2023-03-29 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0015_transaction_history_timestamp"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction_history",
            name="month",
            field=models.CharField(default="3", max_length=100),
        ),
        migrations.AlterField(
            model_name="transaction_history",
            name="timestamp",
            field=models.DateTimeField(default="2023-03-30 02:22:21.116389"),
        ),
    ]
