#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : simple_app/models.py
# Author            : duino <472365351duino@gmail.com>
# Date              : 21.07.2018
# Last Modified Date: 21.07.2018
# Last Modified By  : duino <472365351duino@gmail.com>
from django.db import models
from datetime import datetime


# Create your models here.
class Message(models.Model):
    #user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    message = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)


class ProjectTable(models.Model):
    project_id = models.CharField(max_length=100, default="")
    contract_id = models.CharField(max_length=100, default="")
    table_id = models.CharField(max_length=100, default="")
    company_name = models.CharField(max_length=100, default="")
    project_name = models.CharField(max_length=100, default="")
    contract_project_name = models.CharField(max_length=100, default="")
    new_table_koujing = models.CharField(max_length=100, default="")
    construct_company = models.CharField(max_length=100, default="")
    project_group = models.CharField(max_length=100, default="")
    construct_person = models.CharField(max_length=100, default="")
    quality_person = models.CharField(max_length=100, default="")
    install_method = models.CharField(max_length=100, default="")
    product_manager = models.CharField(max_length=100, default="")
    financial_check = models.CharField(max_length=100, default="")
    chairman_check = models.CharField(max_length=100, default="")
    client_address = models.CharField(max_length=100, default="")
    client_phone = models.CharField(max_length=100, default="")

    create_date = models.CharField(max_length=100, default="")
    project_deadline = models.CharField(max_length=100, default="")
    product_deadline = models.CharField(max_length=100, default="")
    quality_deadline = models.CharField(max_length=100, default="")
    compute_deadline = models.CharField(max_length=100, default="")
    remark = models.TextField(default="")

    print_times = models.IntegerField(default=0)
    contract_money = models.FloatField(default=0.0)
    money_get_previous = models.FloatField(default=0.0)
    plan_money = models.FloatField(default=0.0)
