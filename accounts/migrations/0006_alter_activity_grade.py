# Generated by Django 3.2.1 on 2021-05-07 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_user_id_activity_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='grade',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
