# Generated by Django 4.1.1 on 2023-11-04 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Reciever",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("wallet", models.CharField(max_length=100)),
                ("signature", models.CharField(max_length=1000)),
                ("items", models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product_name", models.CharField(blank=True, max_length=100)),
                ("product_description", models.CharField(blank=True, max_length=500)),
                ("currency", models.CharField(max_length=100)),
                ("amount", models.FloatField()),
                (
                    "reciever",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pay_system.reciever",
                    ),
                ),
            ],
        ),
    ]
