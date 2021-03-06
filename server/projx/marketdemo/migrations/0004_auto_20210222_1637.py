# Generated by Django 3.1.7 on 2021-02-22 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketdemo', '0003_auto_20210221_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='land',
            name='location_id',
            field=models.ForeignKey(blank=True, db_column='location_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='location', to='marketdemo.location'),
        ),
    ]
