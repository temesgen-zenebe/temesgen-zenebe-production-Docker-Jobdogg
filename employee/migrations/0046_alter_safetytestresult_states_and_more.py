# Generated by Django 4.2 on 2023-07-18 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0045_alter_videoresume_states_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='safetytestresult',
            name='states',
            field=models.CharField(default='success', max_length=20),
        ),
        migrations.AlterField(
            model_name='videoresume',
            name='tell_about_you',
            field=models.TextField(max_length=600, null=True),
        ),
    ]
