#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : simple_app/schema.py
# Author            : duino <472365351duino@gmail.com>
# Date              : 21.07.2018
# Last Modified Date: 21.07.2018
# Last Modified By  : duino <472365351duino@gmail.com>
import graphene
from graphene_django.types import DjangoObjectType
from . import models
from django.db.models import Q

#############
#  Message  #
#############

class MessageType(DjangoObjectType):
    class Meta:
        model = models.Message
        interfaces = (graphene.Node, )


class Query(graphene.AbstractType):
    all_messages = graphene.List(MessageType)
    message = graphene.Field(MessageType, id=graphene.ID())
    messagesum = graphene.Int()

    def resolve_all_messages(self, args, **kwargs): #context, info):
        return models.Message.objects.all()

    def resolve_messagesum(self, info):
        return len(models.Message.objects.all());


class CreateMessage(graphene.Mutation):
    message = graphene.String()

    class Arguments:
        message = graphene.String()

    def mutate(self, info, message):
        message = models.Message(message=message)
        message.save()
        return CreateMessage(
            message=message.message,
        )


##################
#  ProjectTable  #
##################
# type
class ProjectTableType(DjangoObjectType):
    class Meta:
        model = models.ProjectTable
        interfaces = (graphene.Node, )

# query
class Query(graphene.AbstractType):
    projecttablesum = graphene.Int()
    projecttables = graphene.List(ProjectTableType, 
                                  companyName=graphene.String(),
                                  createDate=graphene.String(),
                                  projectName=graphene.String(),
                                  projectId=graphene.String(),
                                  contractProjectName=graphene.String(),
                                  clientAddress=graphene.String(),
                                  constructCompany=graphene.String(),
                                  constructPerson=graphene.String(),
                                  projectGroup=graphene.String(),
                                  contractMoney=graphene.String(),
                                  moneyGetPrevious=graphene.String(),
                                  planMoney=graphene.String(),
                                  )
    table = graphene.List(ProjectTableType, 
                           tableId=graphene.String())

    def resolve_projecttablesum(self, info):
        return len(models.ProjectTable.objects.all());

    def resolve_table(self, info, tableId):
        print("tableId: ", tableId)
        return models.ProjectTable.objects.filter(Q(table_id__icontains=tableId));

    def resolve_projecttables(self, info, **kwargs):
        objs = models.ProjectTable.objects.all()

        company_name = kwargs["companyName"]
        create_date = kwargs["createDate"]
        project_name = kwargs["projectName"]
        project_id = kwargs["projectId"]
        contract_project_name = kwargs["contractProjectName"]
        client_address = kwargs["clientAddress"]
        construct_company = kwargs["constructCompany"]
        construct_person = kwargs["constructPerson"]
        project_group = kwargs["projectGroup"]
        contract_money = kwargs["contractMoney"]
        money_get_previous = kwargs["moneyGetPrevious"]
        plan_money = kwargs["planMoney"]

        if company_name != "":
            objs = objs.filter(company_name__icontains=company_name)
        if create_date != "":
            objs = objs.filter(create_date__icontains=create_date)
        if project_name != "":
            objs = objs.filter(project_name__icontains=project_name)
        if project_id != "":
            objs = objs.filter(project_id__icontains=project_id)
        if contract_project_name != "":
            objs = objs.filter(contract_project_name__icontains=contract_project_name)
        if client_address != "":
            objs = objs.filter(client_address__icontains=client_address)
        if construct_company != "":
            objs = objs.filter(construct_company__icontains=construct_company)
        if construct_person != "":
            objs = objs.filter(construct_person__icontains=construct_person)
        if project_group != "":
            objs = objs.filter(project_group__icontains=project_group)

        if contract_money != "":
            contract_money = float(contract_money)
            objs = objs.filter(contract_money__icontains=contract_money)
        if money_get_previous != "":
            money_get_previous = float(money_get_previous)
            objs = objs.filter(money_get_previous__icontains=money_get_previous)
        if plan_money != "":
            plan_money = float(plan_money)
            objs = objs.filter(plan_money__icontains=plan_money)
        return objs;


# mutation
class CreateTable(graphene.Mutation):
    contract_id = graphene.String()
    project_id = graphene.String()
    table_id = graphene.String()
    company_name = graphene.String()
    project_name = graphene.String()
    contract_project_name = graphene.String()
    new_table_koujing = graphene.String()
    construct_company = graphene.String()
    project_group = graphene.String()
    install_method = graphene.String()
    client_address = graphene.String()
    remark = graphene.String()
    client_phone = graphene.String()

    construct_person = graphene.String()
    quality_person = graphene.String()
    product_manager = graphene.String()
    financial_check = graphene.String()
    chairman_check = graphene.String()

    create_date = graphene.String()
    project_deadline = graphene.String() 
    product_deadline = graphene.String() 
    quality_deadline = graphene.String() 
    compute_deadline = graphene.String() 

    plan_money = graphene.Float()
    contract_money = graphene.Float()
    money_get_previous = graphene.Float()
    print_times = graphene.Int()

    class Arguments:
        contract_id = graphene.String()
        project_id = graphene.String()
        table_id = graphene.String()
        company_name = graphene.String()
        project_name = graphene.String()
        contract_project_name = graphene.String()
        new_table_koujing = graphene.String()
        construct_company = graphene.String()
        project_group = graphene.String()
        install_method = graphene.String()
        client_address = graphene.String()
        remark = graphene.String()
        construct_person = graphene.String()
        quality_person = graphene.String()
        product_manager = graphene.String()
        financial_check = graphene.String()
        chairman_check = graphene.String()
        client_phone = graphene.String()
        create_date = graphene.String()
        project_deadline = graphene.String() 
        product_deadline = graphene.String() 
        quality_deadline = graphene.String() 
        compute_deadline = graphene.String() 
        plan_money = graphene.Float()
        contract_money = graphene.Float()
        money_get_previous = graphene.Float()
        print_times = graphene.Int()

    def mutate(self, info, **kwargs):
        table = models.ProjectTable(
            contract_id = kwargs['contract_id'], # 12
            project_id = kwargs['project_id'],
            table_id = kwargs['table_id'],
            company_name = kwargs['company_name'],
            project_name = kwargs['project_name'],
            contract_project_name = kwargs['contract_project_name'],
            new_table_koujing = kwargs['new_table_koujing'],
            construct_company = kwargs['construct_company'],
            project_group = kwargs['project_group'],
            install_method = kwargs['install_method'],
            client_address = kwargs['client_address'],
            remark = kwargs['remark'],
            construct_person = kwargs['construct_person'], # 5
            quality_person = kwargs['quality_person'],
            product_manager = kwargs['product_manager'],
            financial_check = kwargs['financial_check'],
            chairman_check = kwargs['chairman_check'],
            create_date = kwargs['create_date'], # 5
            project_deadline = kwargs['project_deadline'], 
            product_deadline = kwargs['product_deadline'], 
            quality_deadline = kwargs['quality_deadline'], 
            compute_deadline = kwargs['compute_deadline'], 
            client_phone = kwargs['client_phone'], # 5
            plan_money = kwargs['plan_money'],
            contract_money = kwargs['contract_money'],
            money_get_previous = kwargs['money_get_previous'],
            print_times = kwargs['print_times'],
        )
        table.save()
        return CreateTable(
            contract_id = table.contract_id,
            project_id = table.project_id,
            table_id = table.table_id,
            company_name = table.company_name,
            project_name = table.project_name,
            contract_project_name = table.contract_project_name,
            new_table_koujing = table.new_table_koujing,
            construct_company = table.construct_company,
            project_group = table.project_group,
            install_method = table.install_method,
            client_address = table.client_address,
            remark = table.remark,
            construct_person = table.construct_person,
            quality_person = table.quality_person,
            product_manager = table.product_manager,
            financial_check = table.financial_check,
            chairman_check = table.chairman_check,
            create_date = table.create_date,
            project_deadline = table.project_deadline, 
            product_deadline = table.product_deadline, 
            quality_deadline = table.quality_deadline, 
            compute_deadline = table.compute_deadline, 
            client_phone = table.client_phone,
            plan_money = table.plan_money,
            contract_money = table.contract_money,
            money_get_previous = table.money_get_previous,
            print_times = table.print_times,
        )


class EditTable(graphene.Mutation):
    contract_id = graphene.String()
    project_id = graphene.String()
    table_id = graphene.String()
    company_name = graphene.String()
    project_name = graphene.String()
    contract_project_name = graphene.String()
    new_table_koujing = graphene.String()
    construct_company = graphene.String()
    project_group = graphene.String()
    install_method = graphene.String()
    client_address = graphene.String()
    remark = graphene.String()
    client_phone = graphene.String()

    construct_person = graphene.String()
    quality_person = graphene.String()
    product_manager = graphene.String()
    financial_check = graphene.String()
    chairman_check = graphene.String()

    create_date = graphene.String()
    project_deadline = graphene.String() 
    product_deadline = graphene.String() 
    quality_deadline = graphene.String() 
    compute_deadline = graphene.String() 

    plan_money = graphene.Float()
    contract_money = graphene.Float()
    money_get_previous = graphene.Float()
    print_times = graphene.Int()

    class Arguments:
        contract_id = graphene.String()
        project_id = graphene.String()
        table_id = graphene.String()
        company_name = graphene.String()
        project_name = graphene.String()
        contract_project_name = graphene.String()
        new_table_koujing = graphene.String()
        construct_company = graphene.String()
        project_group = graphene.String()
        install_method = graphene.String()
        client_address = graphene.String()
        remark = graphene.String()
        construct_person = graphene.String()
        quality_person = graphene.String()
        product_manager = graphene.String()
        financial_check = graphene.String()
        chairman_check = graphene.String()
        client_phone = graphene.String()
        create_date = graphene.String()
        project_deadline = graphene.String() 
        product_deadline = graphene.String() 
        quality_deadline = graphene.String() 
        compute_deadline = graphene.String() 
        plan_money = graphene.Float()
        contract_money = graphene.Float()
        money_get_previous = graphene.Float()
        print_times = graphene.Int()

    def mutate(self, info, **kwargs):
        table = models.ProjectTable.objects.get(table_id=kwargs['table_id'])
        table.contract_id = kwargs['contract_id']
        table.project_id = kwargs['project_id']
        table.company_name = kwargs['company_name']
        table.project_name = kwargs['project_name']
        table.contract_project_name = kwargs['contract_project_name']
        table.new_table_koujing = kwargs['new_table_koujing']
        table.construct_company = kwargs['construct_company']
        table.project_group = kwargs['project_group']
        table.install_method = kwargs['install_method']
        table.client_address = kwargs['client_address']
        table.remark = kwargs['remark']
        table.construct_person = kwargs['construct_person']
        table.quality_person = kwargs['quality_person']
        table.product_manager = kwargs['product_manager']
        table.financial_check = kwargs['financial_check']
        table.chairman_check = kwargs['chairman_check']
        table.create_date = kwargs['create_date']
        table.project_deadline = kwargs['project_deadline'],
        table.product_deadline = kwargs['product_deadline'],
        table.quality_deadline = kwargs['quality_deadline'],
        table.compute_deadline = kwargs['compute_deadline'],
        table.client_phone = kwargs['client_phone']
        table.plan_money = kwargs['plan_money']
        table.contract_money = kwargs['contract_money']
        table.money_get_previous = kwargs['money_get_previous']
        table.print_times = kwargs['print_times']
        table.save()

        return EditTable(
            contract_id = table.contract_id,
            project_id = table.project_id,
            table_id = table.table_id,
            company_name = table.company_name,
            project_name = table.project_name,
            contract_project_name = table.contract_project_name,
            new_table_koujing = table.new_table_koujing,
            construct_company = table.construct_company,
            project_group = table.project_group,
            install_method = table.install_method,
            client_address = table.client_address,
            remark = table.remark,
            construct_person = table.construct_person,
            quality_person = table.quality_person,
            product_manager = table.product_manager,
            financial_check = table.financial_check,
            chairman_check = table.chairman_check,
            create_date = table.create_date,
            project_deadline = table.project_deadline, 
            product_deadline = table.product_deadline, 
            quality_deadline = table.quality_deadline, 
            compute_deadline = table.compute_deadline, 
            client_phone = table.client_phone,
            plan_money = table.plan_money,
            contract_money = table.contract_money,
            money_get_previous = table.money_get_previous,
            print_times = table.print_times,
        )


class Mutation(graphene.ObjectType):
    create_message = CreateMessage.Field()
    create_table = CreateTable.Field()
    edit_table = EditTable.Field()
