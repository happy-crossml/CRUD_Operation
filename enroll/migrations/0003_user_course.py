# Generated by Django 4.2.3 on 2023-07-06 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_alter_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='course',
            field=models.CharField(default=1, max_length=125),
            preserve_default=False,
        ),
    ]