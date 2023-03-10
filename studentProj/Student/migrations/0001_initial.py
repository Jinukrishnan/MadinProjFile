# Generated by Django 4.1.5 on 2023-01-18 00:34

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('C_slug', models.SlugField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('D_name', models.CharField(max_length=250, unique=True)),
                ('D_slug', models.SlugField(max_length=250, unique=True)),
                ('D_image', models.ImageField(upload_to='department')),
                ('Vacancy', models.IntegerField()),
                ('Description', models.TextField()),
                ('Vision', models.TextField()),
                ('Mission', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('genter', models.CharField(max_length=100)),
                ('phone', models.DecimalField(decimal_places=10, max_digits=20)),
                ('email', models.CharField(max_length=250)),
                ('address', models.TextField()),
                ('Purpose', models.CharField(max_length=250)),
                ('Material', models.CharField(max_length=250)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.department')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.department'),
        ),
    ]
