# Generated by Django 2.2 on 2020-03-19 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listeningGame', '0002_auto_20200319_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listeninggamedata',
            name='email',
        ),
        migrations.RemoveField(
            model_name='listeninggamedata',
            name='id',
        ),
        migrations.AddField(
            model_name='listeninggamedata',
            name='emailId',
            field=models.EmailField(default='', max_length=100, primary_key=True, serialize=False),
        ),
    ]
