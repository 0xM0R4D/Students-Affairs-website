# Generated by Django 3.2.6 on 2022-05-15 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stuinfos', '0006_auto_20220515_0448'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=30)),
                ('course_hours', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='coursestudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='stu',
            fields=[
                ('stu_name', models.CharField(max_length=30)),
                ('GPA', models.FloatField()),
                ('stu_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
