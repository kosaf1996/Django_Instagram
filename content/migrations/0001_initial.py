# Generated by Django 3.2.8 on 2022-03-02 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('image', models.TextField()),
                ('profile_image', models.TextField()),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='email')),
                ('user_id', models.CharField(blank=True, max_length=30, null=True)),
                ('like_count', models.IntegerField()),
            ],
        ),
    ]
