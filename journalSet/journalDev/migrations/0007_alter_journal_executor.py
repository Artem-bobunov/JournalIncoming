# Generated by Django 3.2.13 on 2022-11-21 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalDev', '0006_alter_journal_perfomance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='executor',
            field=models.CharField(blank=True, choices=[('А.А. Александров', 'А.А. Александров'), ('А.А. Бакулин', 'А.А. Бакулин'), ('Ю.А. Деточенко', 'Ю.А. Деточенко'), ('С.К. Меликян', 'С.К. Меликян'), ('О.Ю. Кошелева', 'О.Ю. Кошелева'), ('А.В. Бобунов', 'А.В. Бобунов')], max_length=100, null=True, verbose_name='Исполнитель'),
        ),
    ]
