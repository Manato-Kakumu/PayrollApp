from django import forms 
from .models import Payroll, Salary
import datetime

class PayrollForm(forms.ModelForm):

    class Meta:
        model = Payroll
        fields = '__all__'

    dt = datetime.datetime.today()
    dt = dt.date()

    # 授業報告(日付、生徒名、授業時間、PS2、高1,2年、高3年)
    # teacher_name = forms.CharField(max_length=10, label="講師名")
    date = forms.DateField(label="日付", required=False, initial=dt)
    student1_1 = forms.CharField(max_length=10, label="生徒名1(15:15～16:45)", required=False)
    student1_2 = forms.CharField(max_length=10, label="生徒名2(15:15～16:45)", required=False)
    student2_1 = forms.CharField(max_length=10, label="生徒名1(16:50～18:20)", required=False)
    student2_2 = forms.CharField(max_length=10, label="生徒名2(16:50～18:20)", required=False)
    student3_1 = forms.CharField(max_length=10, label="生徒名1(18:25～19:55)", required=False)
    student3_2 = forms.CharField(max_length=10, label="生徒名2(18:25～19:55)", required=False)
    student4_1 = forms.CharField(max_length=10, label="生徒名1(20:00～21:30)", required=False)
    student4_2 = forms.CharField(max_length=10, label="生徒名2(20:00～21:30)", required=False)

    class_time = forms.FloatField(label="授業時間", required=False)
    PS2_time = forms.FloatField(label="PS2時間", required=False)
    high12_time = forms.FloatField(label="高校1,2年生の授業回数", required=False)
    high3_time = forms.FloatField(label="高校3年生の授業回数", required=False)

    # 事務給(単元テスト、テスト講評、その他)
    unit_test = forms.IntegerField(label="単元テスト回数", required=False)
    test_review = forms.IntegerField(label="テスト講評回数", required=False)
    others = forms.FloatField(label="その他の事務時間", required=False)


class SalaryForm(forms.ModelForm):

    class Meta:
        model =Salary
        fields = '__all__'