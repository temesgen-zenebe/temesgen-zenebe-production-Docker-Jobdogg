# Generated by Django 4.2 on 2023-09-10 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0061_alter_basicinformation_apartment'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificationlicense',
            name='document_type',
            field=models.CharField(choices=[('CERTIFICATION', 'CERTIFICATION'), ('LICENSES', 'LICENSES')], default='certification', max_length=100),
        ),
        migrations.AddField(
            model_name='education',
            name='documentation',
            field=models.BooleanField(default=False),
        ),
    ]
