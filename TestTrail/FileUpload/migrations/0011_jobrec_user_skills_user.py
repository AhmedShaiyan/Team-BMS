# Generated by Django 4.2.1 on 2023-07-24 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FileUpload', '0010_jobrec_job_recs'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobrec',
            name='user',
            field=models.CharField(default='test', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='user',
            field=models.CharField(default='test', max_length=500),
            preserve_default=False,
        ),
    ]