# Generated by Django 3.1.5 on 2021-03-04 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='num_stars',
            field=models.IntegerField(choices=[(1, 'Normal'), (2, 'Bad'), (3, 'Worse'), (4, 'Good'), (5, 'Excellent')]),
        ),
    ]
