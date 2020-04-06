from django.db import models

# Create your models here.


class Specialty(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(verbose_name='Код', max_length=300)
    title = models.CharField(verbose_name='Название специализации', max_length=300)
    picture = models.CharField(verbose_name='Изображение', max_length=300, default='', null=True,)

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'

    def __str__(self):
        return self.title


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Название компании', max_length=300)
    location = models.CharField(verbose_name='Город', max_length=300, default='', null=True,)
    logo = models.CharField(verbose_name='Логотип', max_length=300, default='', null=True,)
    description = models.TextField(verbose_name='Описание', default='', null=True,)
    employee_count = models.PositiveIntegerField(verbose_name='Количество сотрудников', default=0)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='Название вакансии', max_length=300)
    specialty = models.ForeignKey(Specialty, verbose_name='Специализация', on_delete=models.SET_NULL, null=True,
                                  related_name='vacancy_speciality')
    company = models.ForeignKey(Company, verbose_name='Компания', on_delete=models.CASCADE,
                                related_name='company_name', unique=False)
    skills = models.CharField(verbose_name='Скилы', max_length=300, default='')
    description = models.TextField(verbose_name='Описание')
    salary_min = models.PositiveIntegerField(verbose_name='Минимальная з/п')
    salary_max = models.PositiveIntegerField(verbose_name='Максимальная з/п')
    published_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title + ' ' + self.company.name

# """ Вакансии """
#
# jobs = [
#
#     {"title": "Разработчик на Python", "cat": "backend", "company": "staffingsmarter", "salary_from": "100000",
#      "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"},
#     {"title": "Разработчик в проект на Django", "cat": "backend", "company": "swiftattack", "salary_from": "80000",
#      "salary_to": "90000", "posted": "2020-03-11", "desc": "Потом добавим"},
#     {"title": "Разработчик на Swift в аутсорс компанию", "cat": "backend", "company": "swiftattack",
#      "salary_from": "120000", "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"},
#     {"title": "Мидл программист на Python", "cat": "backend", "company": "workiro", "salary_from": "80000",
#      "salary_to": "90000", "posted": "2020-03-11", "desc": "Потом добавим"},
#     {"title": "Питонист в стартап", "cat": "backend", "company": "primalassault", "salary_from": "120000",
#      "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"}
#
# ]
#
# """ Компании """
#
# companies = [
#
#     {"title": "workiro"},
#     {"title": "rebelrage"},
#     {"title": "staffingsmarter"},
#     {"title": "evilthreat h"},
#     {"title": "wirey "},
#     {"title": "swiftattack"},
#     {"title": "troller"},
#     {"title": "primalassault"}
#
# ]
#
# """ Категории """
#
# specialties = [
#
#     {"code": "frontend", "title": "Фронтенд"},
#     {"code": "backend", "title": "Бэкенд"},
#     {"code": "gamedev", "title": "Геймдев"},
#     {"code": "devops", "title": "Девопс"},
#     {"code": "design", "title": "Дизайн"},
#     {"code": "products", "title": "Продукты"},
#     {"code": "management", "title": "Менеджмент"},
#     {"code": "testing", "title": "Тестирование"},
#     {"code": "ios", "title": "Разработка под iOS"},
#     {"code": "android", "title": "Разработка под Android"}
#
# ]
# for x in specialties:
#     spec = Specialty.objects.create(code=x['code'], title=x['title'])
#
# for x in companies:
#     comp = Company.objects.create(name=x['title'])
#
# for x in jobs:
#     vacancy = Vacancy.objects.create(title=x["title"], specialty=Specialty.objects.get(code=x["cat"]), company=Company.objects.get(name=x["company"]), salary_min=x["salary_from"],
#      salary_max=x["salary_to"], published_at=x["posted"], description=x["desc"])
