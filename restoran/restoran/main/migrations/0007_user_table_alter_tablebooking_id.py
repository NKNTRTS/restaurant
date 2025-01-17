# Generated by Django 4.2.11 on 2024-04-13 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_tablebooking_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='table',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.tablebooking'),
        ),
        migrations.AlterField(
            model_name='tablebooking',
            name='id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
    ]
