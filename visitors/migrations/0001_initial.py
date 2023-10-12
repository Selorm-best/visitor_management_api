# Generated by Django 4.2.6 on 2023-10-12 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('organization', models.CharField(max_length=255)),
                ('contact_details', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose_of_visit', models.TextField()),
                ('time_visited', models.DateTimeField(auto_now_add=True)),
                ('time_departed', models.DateTimeField(auto_now_add=True)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitors.destination')),
                ('visitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitors.visitor')),
            ],
        ),
    ]
