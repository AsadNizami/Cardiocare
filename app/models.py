from django.db import models
from django.contrib.auth.models import User


class Test(models.Model):
    CHOICES = ((1, 'Male'), (0, 'Female'))
    THAL = ((0, 'Normal'), (1, 'Fixed Defect'), (2, 'Revesable Defect'))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    sex = models.IntegerField(choices=CHOICES)
    cp = models.IntegerField()
    trestbps = models.IntegerField()
    chol = models.IntegerField()
    restecg = models.IntegerField()
    thalach = models.IntegerField()
    exang = models.IntegerField()
    oldpeak = models.IntegerField()
    slope = models.IntegerField()
    ca = models.IntegerField()
    thal = models.IntegerField(choices=THAL)
    date = models.DateTimeField(blank=True)
    result = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f'{self.user.username} Test {self.date.strftime("%H %B %d")}'
