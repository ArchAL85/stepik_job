from django.shortcuts import render
from django.views import View
from django.db.models import Count

from job.models import Specialty, Vacancy, Company

# Create your views here.

class MainView(View):
    template_name = 'index.html'

    def get(self, request):
        company_count = Vacancy.objects.values('company').annotate(count=Count('company'))\
            .values_list('company__name', 'company__logo', 'count', 'company__id')
        vacancy_count = Vacancy.objects.values('specialty').annotate(count=Count('specialty'))\
            .values_list('specialty__title', 'specialty__picture', 'specialty__code', 'count')
        return render(request, self.template_name, {'company_count': company_count, 'vacancy_count': vacancy_count})


class AllVacanciesView(View):
    template_name = 'list.html'

    def get(self, request):
        vacancies_dict = Vacancy.objects.all()
        vacancies_count = vacancies_dict.count()
        vacancies = [{'specialty__title': 'Все вакансии', 'count': vacancies_count, 'vacancies': vacancies_dict}]
        return render(request, self.template_name, {'vacancies': vacancies})


class JobCatView(View):
    template_name = 'list.html'

    def get(self, request, category_title):
        vacancies = Vacancy.objects.filter(specialty__code=category_title).values('specialty__title')\
            .annotate(count=Count('specialty__title'))
        for vacancies_dict in vacancies:
            vacancies_dict['vacancies'] = Vacancy.objects.filter(specialty__title=vacancies_dict['specialty__title'])
        return render(request, self.template_name, {'vacancies': vacancies})


class CompanyView(View):
    template_name = 'company.html'

    def get(self, request, company_id):
        company = Company.objects.filter(id=company_id).values('name')
        vacancies = Vacancy.objects.filter(company__id=company_id)
        vacancies_count = vacancies.count()
        return render(request, self.template_name, {'company': company, 'vacancies': vacancies, 'count': vacancies_count})


class JobView(View):
    template_name = 'vacancy.html'

    def get(self, request, job_id):
        vacancy = Vacancy.objects.get(id=job_id)
        return render(request, self.template_name, {'vacancy': vacancy})
