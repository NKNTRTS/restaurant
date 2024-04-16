from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_tablebooking_time_alter_dish_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablebooking',
            name='date',
            field=models.DateField(default=None),
        ),
    ]
