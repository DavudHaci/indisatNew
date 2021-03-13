# Generated by Django 3.0.7 on 2020-09-22 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20200918_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='nomre',
            field=models.CharField(default=2, max_length=13, verbose_name='Telfon Nomresi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='qiymet',
            field=models.CharField(default=1, max_length=11, verbose_name='Qiymet'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('e', 'Elektronika'), ('evb', 'Ev Ve Bag'), ('g', 'geyim')], default='', max_length=3),
        ),
    ]