# Generated by Django 3.2.13 on 2022-11-17 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalDev', '0002_auto_20221117_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='executor',
            field=models.CharField(choices=[('А.А. Александров', 'А.А. Александров'), ('А.А. Бакулин', 'А.А. Бакулин'), ('Ю.А. Деточенко', 'Ю.А. Деточенко'), ('С.К. Меликян', 'С.К. Меликян')], max_length=100, null=True, verbose_name='Исполнитель'),
        ),
    ]
