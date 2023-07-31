from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Journal(models.Model):
    us = (
    ('А.А. Александров','А.А. Александров'),
    ('А.А. Бакулин','А.А. Бакулин'),
    ('Ю.А. Деточенко','Ю.А. Деточенко'),
    ('С.К. Меликян','С.К. Меликян'),
    ('О.Ю. Кошелева','О.Ю. Кошелева'),
    ('Д.В. Никитин','Д.В. Никитин'),
    ('А.В. Бобунов','А.В. Бобунов'),
    )
    mark_perfomance = (
         ('информация обработана','информация обработана'),
         ('исполнено','исполнено'),
         ('принято к сведению','принято к сведению'),
         ('рассмотрено','рассмотрено'),
         ('Размещено на сайте','Размещено на сайте'),
     )
    NC = (
        ('07-01','07-01'),('07-02','07-02'),('07-03','07-03'),('07-04','07-04'),('07-05','07-05'),('07-06','07-06'),('07-07','07-07'),
        ('07-08','07-08'),('07-09','07-09'),('07-10','07-10'),('07-11','07-11'),('07-12','07-12'),('07-13','07-13'),('07-14','07-14'),
        ('07-15','07-15'),('07-16','07-16'),('07-17','07-17'),('07-18','07-18'),
    )
    reg = models.IntegerField('Регистрационный номер', null=True,blank=True)
    dateInput = models.DateField('дата поступления',null=True,blank=True)
    otKogo = models.CharField('От кого', max_length=1000,null=True,blank=True)
    vxnumber = models.CharField('вх.№',max_length=1000,null=True,blank=True)
    isxnumber = models.CharField('исх.№',max_length=1000,null=True,blank=True)
    summary = models.CharField('Краткое содеражние',max_length=1000,null=True,blank=True)
    executor = models.CharField('Исполнитель',max_length=100,null=True,blank=True,choices=us)
    perfomance = models.CharField('Отметка об исполнении',max_length=1000,null=True,blank=True,choices=mark_perfomance)#choices=mark_perfomance
    control = models.CharField('Признак контроля',max_length=1000,null=True,blank=True)
    answertMail = models.CharField('Ответ на письмо',max_length=1000,null=True,blank=True)
    note = models.CharField('Примечание',max_length=1000,null=True,blank=True)
    nd = models.CharField('НД',choices=NC,max_length=1000,null=True,blank=True)


