# Generated by Django 5.1.1 on 2024-12-06 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_hotelbooking_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelbooking',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='hotelbooking',
            name='room_type',
            field=models.CharField(blank=True, choices=[('AC', 'AC'), ('Non AC', 'Non AC')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='hotelbooking',
            name='total_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='booking_type',
            field=models.CharField(choices=[('pre paid', 'Pre Paid'), ('post paid', 'Post Paid')], max_length=100),
        ),
    ]