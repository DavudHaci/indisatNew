# Generated by Django 3.0.7 on 2020-10-12 08:04

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0020_elanimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elan',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Mehsul Haqqında'),
        ),
        migrations.AlterField(
            model_name='elan',
            name='image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Səkil Əlavə Et'),
        ),
        migrations.AlterField(
            model_name='elan',
            name='nomre',
            field=models.IntegerField(verbose_name='Telefon Nömrəsi'),
        ),
        migrations.AlterField(
            model_name='elan',
            name='qiymet',
            field=models.IntegerField(verbose_name='Qiymət'),
        ),
        migrations.AlterField(
            model_name='elan',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Başlıq Yazısı '),
        ),
        migrations.AlterField(
            model_name='elan',
            name='user',
            field=models.CharField(max_length=50, verbose_name='İsdifadəçi Adı'),
        ),
        migrations.CreateModel(
            name='ElanCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('e', 'Elektronika'), ('evb', 'Ev Ve Bag'), ('se', 'Sexsi Esyalar'), ('n', 'Neqliyat'), ('da', 'Dasinmaz Emlak'), ('hvn', 'Heyvanlar'), ('tlf', 'Telefonlar')], max_length=50, verbose_name='Category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Elan')),
            ],
        ),
    ]
