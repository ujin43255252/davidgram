# Generated by Django 2.0.4 on 2018-04-17 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180418_0559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('female', 'Female'), ('not-specified', 'Not specified'), ('male', 'Male')], max_length=80, null=True),
        ),
    ]