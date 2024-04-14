# Generated by Django 4.2.11 on 2024-04-03 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('number', models.CharField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('number', models.CharField(primary_key=True, serialize=False)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField()),
                ('enrollment', models.ManyToManyField(to='university.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.room'),
        ),
    ]