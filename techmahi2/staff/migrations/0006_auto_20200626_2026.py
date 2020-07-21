# Generated by Django 2.2.12 on 2020-06-26 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_auto_20200625_1842'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee_history',
            old_name='period_of_service_from',
            new_name='employee_service_from',
        ),
        migrations.RenameField(
            model_name='employee_history',
            old_name='period_of_service_to',
            new_name='employee_service_to',
        ),
        migrations.AlterField(
            model_name='employee',
            name='e_salary_expected',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Salary Expected'),
        ),
    ]