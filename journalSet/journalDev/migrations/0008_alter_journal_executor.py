# Generated by Django 3.2.11 on 2023-06-01 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalDev', '0007_alter_journal_executor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='executor',
            field=models.CharField(blank=True, choices=[('А.А. Александров', 'А.А. Александров'), ('А.А. Бакулин', 'А.А. Бакулин'), ('Ю.А. Деточенко', 'Ю.А. Деточенко'), ('С.К. Меликян', 'С.К. Меликян'), ('О.Ю. Кошелева', 'О.Ю. Кошелева'), ('А.В. Бобунов', 'А.В. Бобунов'), ('Д.В. Никитин', 'Д.В. Никитин')], max_length=100, null=True, verbose_name='Исполнитель'),
        ),
    ]
