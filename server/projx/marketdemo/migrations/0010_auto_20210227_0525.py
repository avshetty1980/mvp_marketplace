# Generated by Django 3.1.7 on 2021-02-27 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketdemo', '0009_auto_20210226_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='location_id',
        ),
        migrations.AddField(
            model_name='buyer',
            name='location_id',
            field=models.ForeignKey(blank=True, db_column='location_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyer_location', to='marketdemo.location'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='location_id',
            field=models.ForeignKey(blank=True, db_column='location_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transport_location', to='marketdemo.location'),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date_Created'),
        ),
        migrations.AlterField(
            model_name='land',
            name='location_id',
            field=models.ForeignKey(blank=True, db_column='location_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller_location', to='marketdemo.location'),
        ),
        migrations.AlterField(
            model_name='order',
            name='buyer_id',
            field=models.ForeignKey(db_column='buyer_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buyer_order', to='marketdemo.buyer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_id',
            field=models.ForeignKey(db_column='payment_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment_order', to='marketdemo.escrow'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_id',
            field=models.ForeignKey(db_column='product_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_order', to='marketdemo.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='reg_no',
            field=models.ForeignKey(db_column='reg_no', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reg_order', to='marketdemo.delivery'),
        ),
        migrations.AlterField(
            model_name='order',
            name='seller_id',
            field=models.ForeignKey(db_column='seller_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='seller_order', to='marketdemo.seller'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Food', 'Food'), ('Cash', 'Cash'), ('Plantation', 'Plantation'), ('Horticulture', 'Horticulture')], default='Food', max_length=30, verbose_name='Category_of_Crop'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(choices=[('rice', 'rice'), ('wheat', 'wheat'), ('millets', 'millets'), ('pulses', 'pulses'), ('oil', 'oil'), ('seeds', 'seeds'), ('cotton', 'cotton'), ('jute', 'jute')], default='rice', max_length=20, verbose_name='Type_of_Category'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date_Created'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active_Status'),
        ),
    ]
