# Generated by Django 4.2.1 on 2023-07-18 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FileUpload', '0007_alter_skills_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='name',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='FileUpload.document'),
        ),
    ]
