# Generated by Django 4.2.1 on 2023-07-18 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FileUpload', '0006_skills_name_skills_skill_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='FileUpload.document'),
        ),
    ]
