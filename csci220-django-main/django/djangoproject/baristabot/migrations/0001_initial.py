# Generated by Django 4.2.11 on 2024-04-11 13:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField()),
                ('officiality', models.BooleanField()),
                ('description', models.TextField()),
                ('instructions', models.TextField()),
                ('temperature', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('name', models.CharField(primary_key=True, serialize=False)),
                ('caffination', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(primary_key=True, serialize=False)),
                ('password', models.CharField()),
                ('email', models.EmailField(max_length=254)),
                ('created', models.ManyToManyField(related_name='created_drinks', to='baristabot.drink')),
                ('liked', models.ManyToManyField(related_name='liked_drinks', to='baristabot.drink')),
            ],
        ),
        migrations.CreateModel(
            name='Side',
            fields=[
                ('name', models.CharField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('pair_with', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baristabot.drink')),
            ],
        ),
        migrations.AddField(
            model_name='drink',
            name='contains',
            field=models.ManyToManyField(to='baristabot.ingredient'),
        ),
    ]
