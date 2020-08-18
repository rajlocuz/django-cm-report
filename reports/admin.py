from django.contrib import admin
from .models import CISBenchmark, ProwlerOutput, CategoryDetails


# Register your models here.
@admin.register(CISBenchmark)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'check_id', 'check_title', 'aws_config_rule', 'severity', 'observation', 'impact', 'recommendation', 'category_detail']


@admin.register(ProwlerOutput)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'account_id', 'check_id', 'check_title', 'check_output', 'result']


@admin.register(CategoryDetails)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']

