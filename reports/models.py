from django.db import models

# Create your models here.
'''class ProwlerOutput(models.Model):
    RESULT_CHOICES = [
        ('PASS', 'PASS'),
        ('FAIL', 'FAIL'),
        ('INFO', 'INFO'),
    ]
    account_id = models.CharField(max_length=20)
    check_id = models.FloatField()
    check_title = models.CharField(max_length=200)
    check_output = models.TextField()
    result = models.CharField(choices=RESULT_CHOICES, max_length=5)

    def __str__(self):
        return self.check_title
'''


class CategoryDetails(models.Model):
    category = models.CharField(max_length=100)

    # Returning category
    def __str__(self):
        return self.category


class CISBenchmark(models.Model):
    SEVERITY_DETAILS = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical')
    ]
    check_id = models.FloatField()
    check_title = models.CharField(max_length=200)
    severity = models.CharField(choices=SEVERITY_DETAILS, max_length=10)
    aws_config_rule = models.CharField(max_length=100)
    observation = models.CharField(max_length=200)
    impact = models.CharField(max_length=200)
    recommendation = models.TextField()
    category = models.ManyToManyField(CategoryDetails, blank=True)

    # Many to Many field Show in table
    def category_detail(self):
        return ",".join([str(c) for c in self.category.all()])

    def __str__(self):
        return self.check_title


class ProwlerOutput(models.Model):
    status = models.TextField(blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    check_id = models.IntegerField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    score = models.TextField(blank=True, null=True)
    group = models.TextField(blank=True, null=True)
    check_title = models.TextField(blank=True, null=True)
    check_output = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.check_title
