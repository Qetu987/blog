# Generated by Django 3.1.6 on 2021-02-09 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Name')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('name_slug', models.CharField(blank=True, max_length=250, null=True, verbose_name='Name slug')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is published?')),
            ],
        ),
    ]