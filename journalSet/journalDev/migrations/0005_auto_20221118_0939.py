# Generated by Django 3.2.13 on 2022-11-18 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalDev', '0004_auto_20221118_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='executor',
            field=models.CharField(blank=True, choices=[('А.А. Александров', 'А.А. Александров'), ('А.А. Бакулин', 'А.А. Бакулин'), ('Ю.А. Деточенко', 'Ю.А. Деточенко'), ('С.К. Меликян', 'С.К. Меликян'), ('О.Ю. Кошелева', 'О.Ю. Кошелева')], max_length=100, null=True, verbose_name='Исполнитель'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='perfomance',
            field=models.CharField(blank=True, choices=[('информация обработана', 'информация обработана'), ('исполнено', 'исполнено'), ('принято к сведению', 'принято к сведению'), ('рассмотрено', 'рассмотрено')], max_length=1000, null=True, verbose_name='Отметка об исполнении'),
        ),
    ]