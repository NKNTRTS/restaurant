from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_tablebooking'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='group',
            field=models.TextField(default=None),
        ),
    ]
