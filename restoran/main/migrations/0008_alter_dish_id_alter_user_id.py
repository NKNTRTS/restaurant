from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_user_table_alter_tablebooking_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
