# Generated by Django 4.2 on 2023-05-26 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_kingpindrakoclients_kingpindrakoclientsdetails_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kingpindrakoclientsdetails',
            name='pc_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kingpindrakoclientsdetails',
            name='system_applications',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lizzyclientsdetails',
            name='pc_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lizzyclientsdetails',
            name='system_applications',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nadiaclientsdetails',
            name='pc_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nadiaclientsdetails',
            name='system_applications',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='zaaloloclientsdetails',
            name='pc_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='zaaloloclientsdetails',
            name='system_applications',
            field=models.TextField(blank=True, null=True),
        ),
    ]