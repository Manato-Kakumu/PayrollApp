from django.db import models

class Teachers(models.Model):
    teacher_name = models.CharField(max_length=10)
    fare = models.IntegerField()
    sum_salary = models.FloatField(default=0)

    class Meta:
        db_table = "teachers"

    def __str__(self):
        return self.teacher_name

class Payroll(models.Model):
    teacher_name = models.ForeignKey(Teachers, on_delete=models.CASCADE)

    # 授業報告(日付、生徒名、授業時間、PS2、高1,2年、高3年)
    date = models.DateField(null=True)
    student1_1 = models.CharField(null=True, max_length=10)
    student1_2 = models.CharField(null=True, max_length=10)
    student2_1 = models.CharField(null=True, max_length=10)
    student2_2 = models.CharField(null=True, max_length=10)
    student3_1 = models.CharField(null=True, max_length=10)
    student3_2 = models.CharField(null=True, max_length=10)
    student4_1 = models.CharField(null=True, max_length=10)
    student4_2 = models.CharField(null=True, max_length=10)

    class_time = models.FloatField(null=True)
    PS2_time = models.FloatField(null=True)
    high12_time = models.IntegerField(null=True)
    high3_time = models.IntegerField(null=True)

    # 事務給(単元テスト、テスト講評、その他)
    unit_test = models.IntegerField(null=True)
    test_review = models.IntegerField(null=True)
    others = models.FloatField(null=True)

    def __str__(self):
        return '{} {} {} {} {} {} {} {} {}'.format(self.teacher_name, self.student1_1, self.student1_2, self.student2_1, self.student2_2, self.student3_1, self.student3_2, self.student4_1, self.student4_2)
    

class Salary(models.Model):

    teacher_name = models.ForeignKey(Teachers, on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher_name