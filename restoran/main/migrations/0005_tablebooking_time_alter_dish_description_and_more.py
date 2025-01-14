from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_dish_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablebooking',
            name='time',
            field=models.TimeField(default=None),
        ),
        migrations.AlterField(
            model_name='dish',
            name='description',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=10),
        ),
        migrations.AlterField(
            model_name='tablebooking',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AlterField(
            model_name='tablebooking',
            name='table_number',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
