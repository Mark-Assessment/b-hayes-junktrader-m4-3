# Generated by Django 3.2.24 on 2024-02-18 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectables', '0002_glbfile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GLBFile',
        ),
        migrations.AddField(
            model_name='collectable',
            name='glb_file',
            field=models.FileField(blank=True, null=True, upload_to='glb_files/'),
        ),
    ]
