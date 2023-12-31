# Generated by Django 3.2.13 on 2022-11-18 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalDev', '0003_alter_journal_executor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='answertMail',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Ответ на письмо'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='control',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Признак контроля'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='dateInput',
            field=models.DateField(blank=True, null=True, verbose_name='дата поступления'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='executor',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='исполнитель'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='isxnumber',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='исх.№'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='nd',
            field=models.CharField(blank=True, choices=[('07-01', '07-01'), ('07-02', '07-02'), ('07-03', '07-03'), ('07-04', '07-04'), ('07-05', '07-05'), ('07-06', '07-06'), ('07-07', '07-07'), ('07-08', '07-08'), ('07-09', '07-09'), ('07-10', '07-10'), ('07-11', '07-11'), ('07-12', '07-12'), ('07-13', '07-13'), ('07-14', '07-14'), ('07-15', '07-15'), ('07-16', '07-16'), ('07-17', '07-17'), ('07-18', '07-18')], max_length=1000, null=True, verbose_name='НД'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='note',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Примечание'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='otKogo',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='От кого'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='perfomance',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Отметка об исполнении'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='reg',
            field=models.IntegerField(blank=True, null=True, verbose_name='Регистрационный номер'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='summary',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Краткое содеражние'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='vxnumber',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='вх.№'),
        ),
    ]
