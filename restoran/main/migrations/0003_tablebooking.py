from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('table_number', models.IntegerField()),
            ],
        ),
    ]
