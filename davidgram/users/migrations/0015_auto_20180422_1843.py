# Generated by Django 2.0.4 on 2018-04-22 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20180422_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('not-specified', 'Not specified'), ('male', 'Male'), ('female', 'Female')], max_length=80, null=True),
        ),
    ]