# Generated by Django 2.2.3 on 2019-07-10 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=48)),
                ('animation_speed', models.FloatField(default=0.5)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
