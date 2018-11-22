# Generated by Django 2.0 on 2018-11-22 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userforum', '0002_sowingmap'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sowingmap',
            options={'ordering': ['index_images'], 'verbose_name': '轮播图', 'verbose_name_plural': '轮播图'},
        ),
        migrations.AlterField(
            model_name='sowingmap',
            name='images',
            field=models.ImageField(default='sowingmap/default.jpg', upload_to='sowin/%Y%m', verbose_name='轮播图(750X450)'),
        ),
        migrations.AlterField(
            model_name='sowingmap',
            name='index_images',
            field=models.IntegerField(default=0, verbose_name='轮播顺序'),
        ),
    ]
