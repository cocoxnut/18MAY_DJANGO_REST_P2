# Generated by Django 4.0.4 on 2022-05-18 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Basic', 'Basic'), ('Standard', 'Standard'), ('Professional', 'Professional')], max_length=15, verbose_name='Pricing plan')),
                ('price', models.IntegerField(verbose_name='price of plan')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Pricing Plan',
                'verbose_name_plural': 'Pricing Plans',
            },
        ),
    ]
