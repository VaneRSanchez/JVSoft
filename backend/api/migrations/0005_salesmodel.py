# Generated by Django 5.0.1 on 2024-04-03 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_movementtypesmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'sales',
            },
        ),
    ]