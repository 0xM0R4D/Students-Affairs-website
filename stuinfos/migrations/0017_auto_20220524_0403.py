# Generated by Django 3.2.6 on 2022-05-24 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stuinfos', '0016_auto_20220523_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursestudent',
            name='courseNAME',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='coursestudent',
            name='stuID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stuinfos.stu'),
        ),
    ]