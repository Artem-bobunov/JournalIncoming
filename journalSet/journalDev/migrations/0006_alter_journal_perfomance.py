# Generated by Django 3.2.13 on 2022-11-21 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalDev', '0005_auto_20221118_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='perfomance',
            field=models.CharField(blank=True, choices=[('информация обработана', 'информация обработана'), ('исполнено', 'исполнено'), ('принято к сведению', 'принято к сведению'), ('рассмотрено', 'рассмотрено'), ('Размещено на сайте', 'Размещено на сайте')], max_length=1000, null=True, verbose_name='Отметка об исполнении'),
        ),
    ]
