# Generated by Django 4.2 on 2023-06-16 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_kingpindrakoclientsdetails_pc_info_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kingpindrakoclients',
            name='status',
            field=models.CharField(choices=[('ONLINE', 'online'), ('OFFLINE', 'offline')], default='offline', max_length=100),
        ),
        migrations.AlterField(
            model_name='lizzyclients',
            name='status',
            field=models.CharField(choices=[('ONLINE', 'online'), ('OFFLINE', 'offline')], default='offline', max_length=100),
        ),
        migrations.AlterField(
            model_name='nadiaclients',
            name='status',
            field=models.CharField(choices=[('ONLINE', 'online'), ('OFFLINE', 'offline')], default='offline', max_length=100),
        ),
        migrations.AlterField(
            model_name='zaaloloclients',
            name='status',
            field=models.CharField(choices=[('ONLINE', 'online'), ('OFFLINE', 'offline')], default='offline', max_length=100),
        ),
    ]
