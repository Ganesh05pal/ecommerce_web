# Generated by Django 4.1.5 on 2023-01-21 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('lacality', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('zip_code', models.IntegerField()),
                ('state', models.CharField(choices=[('ANDMAN & NICOBAR', 'ANDMAN & NICOBAR'), ('AANDHRA PRADESH', 'AANDHRA PRADESH'), ('BIHAR', 'BIHAR'), ('RAJISHTAN', 'RAJISHTAN'), ('DELHI', 'DELHI'), ('GOA', 'GOA'), ('ASSAM', 'ASSAM'), ('ARUNACHAL PRADESH', 'ARUNACHAL PRADESH')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('decription', models.TextField()),
                ('brand', models.CharField(max_length=100)),
                ('categroy', models.CharField(choices=[('M', 'MOBILE'), ('L', 'LAPTOP'), ('TW', 'TOP WEAR'), ('BW', 'BOTTOM WEAR')], max_length=2)),
                ('Product_image', models.ImageField(upload_to='producting')),
            ],
        ),
        migrations.CreateModel(
            name='OrderedPlaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField(default=1)),
                ('order_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('accepted', 'accepted'), ('packed', 'packed'), ('On the way', 'on the way'), ('deliverd', 'delivered'), ('cencel', 'cencel')], default='pending', max_length=50)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField(default=1)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]