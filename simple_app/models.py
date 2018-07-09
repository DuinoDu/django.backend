from django.db import models

# Create your models here.
class Message(models.Model):
    #user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    message = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)


class ProjectTable(models.Model):
    company_name = models.CharField(max_length=100)
    contract_id = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)
    #project_id = models.CharField(max_length=100)
    #contract_project_name = models.CharField(max_length=100)
    #new_table_koujing = models.CharField(max_length=100)
    #construct_company = models.CharField(max_length=100)
    #project_group = models.CharField(max_length=100)
    #construct_person = models.CharField(max_length=100)
    #quality_person = models.CharField(max_length=100)
    #install_method = models.CharField(max_length=100)
    #table_id = models.CharField(max_length=100)
    #product_manager = models.CharField(max_length=100)
    #financial_check = models.CharField(max_length=100)
    #chairman_check = models.CharField(max_length=100)
    #create_date = models.DateTimeField(auto_now_add=True)
    #project_deadline = models.DateTimeField()
    #product_deadline = models.DateTimeField()
    #quality_deadline = models.DateTimeField()
    #compute_deadline = models.DateTimeField()
    #plan_money = models.FloatField()
    #contract_money = models.FloatField()
    #money_get_previous = models.FloatField()
    #print_times = models.IntegerField()
    #client_phone = models.IntegerField()
    #client_address = models.TextField()
    #remark = models.TextField()
