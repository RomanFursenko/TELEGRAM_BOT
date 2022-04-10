# Generated by Django 4.0.3 on 2022-04-10 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(blank=True, null=True)),
                ('categories', models.TextField(blank=True, null=True)),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
    ]
