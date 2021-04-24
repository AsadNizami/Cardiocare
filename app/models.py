from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Test(models.Model):
    class Meta:
        verbose_name = 'User Test'
        verbose_name_plural = 'User Tests'

    SEX_CHOICES = ((1, 'Male'), (0, 'Female'))
    THAL_CHOICES = ((0, 'Normal'), (1, 'Fixed Defect'), (2, 'Reversible Defect'))
    EXANG_CHOICES = ((0, 'No'), (1, 'Yes'))
    CP_CHOICES = ((0, 'None'), (1, 'Low'), (2, 'Medium'), (3, 'High'))
    CA_CHOICES = ((0, 0), (1, 1), (2, 2), (3, 3))
    RESTECG_CHOICES = ((0, 'Normal'), (1, 'Abnormal'))
    SLOPE_CHOICES = ((0, 0), (1, 1), (2, 2))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField(
        validators=[
            MaxValueValidator(150),
            MinValueValidator(0)
        ]
    )
    sex = models.IntegerField(default='Female', choices=SEX_CHOICES)
    cp = models.IntegerField(default='None', choices=CP_CHOICES)
    trestbps = models.IntegerField(
        validators=[
            MaxValueValidator(250),
            MinValueValidator(50)
        ]
    )
    chol = models.IntegerField(
        validators=[
            MaxValueValidator(600),
            MinValueValidator(100)
        ]
    )
    restecg = models.IntegerField(default='Normal', choices=RESTECG_CHOICES)
    thalach = models.IntegerField(
        validators=[
            MaxValueValidator(250),
            MinValueValidator(50)
        ]
    )
    exang = models.IntegerField(default='No', choices=EXANG_CHOICES)
    oldpeak = models.DecimalField(
        max_digits=5, decimal_places=2,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )
    slope = models.IntegerField(default='0.0-0.2', choices=SLOPE_CHOICES)
    ca = models.IntegerField(default='Normal', choices=CA_CHOICES)
    thal = models.IntegerField(default='Normal', choices=THAL_CHOICES)
    date = models.DateTimeField(blank=True)
    result = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f'{self.user.username.capitalize()}-Test {self.date.strftime("%H:%M - %d %B")}'
