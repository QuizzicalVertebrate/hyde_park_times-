# Generated by Django 4.0.4 on 2022-06-08 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0003_alter_comment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=140),
        ),
    ]
