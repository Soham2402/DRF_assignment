# Generated by Django 4.2.6 on 2023-10-09 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_user_fname_alter_user_lname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]