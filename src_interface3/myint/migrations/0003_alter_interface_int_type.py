# Generated by Django 4.1 on 2022-08-21 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myint', '0002_interface_router_name_alter_interface_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interface',
            name='Int_type',
            field=models.CharField(blank=True, choices=[('ISIS', 'UpLink'), ('IPOSS', 'Uplink'), ('Shut', 'ShutDown'), ('loopBack', 'LoopBack'), ('vlan', 'Vlan'), ('null', 'NULL'), ('vty', 'vty'), ('vlanIF', 'VlanIF')], max_length=12),
        ),
    ]
