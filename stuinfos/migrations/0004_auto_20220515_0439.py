# Generated by Django 3.2.6 on 2022-05-15 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stuinfos', '0003_course_stu'),
    ]

    operations = [
        migrations.DeleteModel(
            name='course',
        ),
        migrations.DeleteModel(
            name='stu',
        ),
    ]
