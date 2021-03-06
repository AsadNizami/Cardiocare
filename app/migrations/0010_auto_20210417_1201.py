# Generated by Django 3.1.7 on 2021-04-17 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_test_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='result_pdf',
            field=models.FileField(blank=True, upload_to='Test_Report'),
        ),
        migrations.AlterField(
            model_name='test',
            name='thal',
            field=models.IntegerField(choices=[(0, 'Normal'), (1, 'Fixed Defect'), (2, 'Reversable Defect')]),
        ),
    ]
