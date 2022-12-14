# Generated by Django 3.2.6 on 2022-05-23 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stuinfos', '0015_course_coursestudent_stu'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coursestudent',
            options={'ordering': ['stuID']},
        ),
        migrations.AlterModelOptions(
            name='stu',
            options={'ordering': ['stu_id']},
        ),
        migrations.AlterField(
            model_name='coursestudent',
            name='courseNAME',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courseid', to='stuinfos.course'),
        ),
        migrations.AlterField(
            model_name='coursestudent',
            name='stuID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentid', to='stuinfos.stu'),
        ),
    ]
