# Generated by Django 3.2.4 on 2021-07-15 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_auto_20210715_1544'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
