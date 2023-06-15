from django.shortcuts import render,redirect

from django.views import View
from .models import Teachers, Payroll
from .forms import PayrollForm, SalaryForm

class HomeView(View):

    def get(self, request, *args, **kwargs):
        form = PayrollForm()

        context = {}
        context["payroll"] = Payroll.objects.all()

        #カテゴリの選択肢を作るため、全てのカテゴリをcontextに引き渡す
        context["teachers"] = Teachers.objects.all()

        return render(request, "home.html", context={
            "form":form,
        })

    def post(self, request, *args, **kwargs):
        form = PayrollForm(request.POST or None)

        if form.is_valid():
            # 給与計算処理
            teacher_name = form.cleaned_data["teacher_name"]
            teacher_info = Teachers.objects.get(teacher_name=teacher_name)
            sum = teacher_info.sum_salary + teacher_info.fare

            class_time = form.cleaned_data["class_time"]
            PS2_time = form.cleaned_data["PS2_time"]
            high12_time = form.cleaned_data["high12_time"]
            high3_time = form.cleaned_data["high3_time"]
            unit_test = form.cleaned_data["unit_test"]
            test_review = form.cleaned_data["test_review"]
            others = form.cleaned_data["others"]
            
            if class_time is not None:
                class_time = class_time * 1000
                sum += class_time
            if PS2_time is not None:
                PS2_time = PS2_time * 200
                sum += PS2_time
            if high12_time is not None:
                high12_time = high12_time * 200 * 1.5
                sum += high12_time
            if high3_time is not None:
                high3_time = high3_time * 300 * 1.5
                sum += high3_time
            if unit_test is not None:
                unit_test = unit_test * 986 * 0.15
                sum += unit_test
            if test_review is not None:
                test_review = test_review * 986 * 0.25
                sum += test_review
            if others is not None:
                others = others * 986
                sum += others
            # print(sum)

            teacher_info.sum_salary = sum
            teacher_info.save()
            form.save()
            form = PayrollForm()

        return render(request, 'home.html', context={
            "form":form,
        })

home = HomeView.as_view()


class SalaryView(View):

    def get(self, request, *args, **kwargs):
        form = SalaryForm()

        context = {}
        context["payroll"] = Payroll.objects.all()

        #カテゴリの選択肢を作るため、全てのカテゴリをcontextに引き渡す
        context["teachers"] = Teachers.objects.all()

        return render(request, "salary.html", context={
            "form":form,
        })

    def post(self, request, *args, **kwargs):
        form = SalaryForm(request.POST or None)

        if form.is_valid():
            teacher_name = form.cleaned_data["teacher_name"]
            teacher_info = Teachers.objects.get(teacher_name=teacher_name)
            sum_salary = teacher_info.sum_salary
            teacher_info.sum_salary = 0
            teacher_info.save()
            form = SalaryForm()
            return render(request, "salary.html", context={
                "salary":sum_salary,
            })
            
        return render(request, 'salary.html', context={
            "form":form,
        })

salary = SalaryView.as_view()