# Generated by Django 4.2.6 on 2023-12-27 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('description', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.customer')),
            ],
        ),
    ]
