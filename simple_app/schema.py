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
    all_projecttables = graphene.List(ProjectTableType)
    projecttables = graphene.List(ProjectTableType, 
            company_name=graphene.String(),
            contract_id=graphene.String(),
            project_name=graphene.String(),)

    def resolve_projecttablesum(self, info):
        return len(models.ProjectTable.objects.all());

    def resolve_all_projecttables(self, info, **kwargs):
        return models.ProjectTable.objects.all();

    def resolve_projecttables(self, info, company_name, contract_id, project_name, **kwargs):
        objs = models.ProjectTable.objects.all()
        if company_name != "":
            objs = objs.filter(company_name__icontains=company_name)
        if contract_id != "":
            objs = objs.filter(contract_id__icontains=contract_id)
        if project_name != "":
            objs = objs.filter(project_name__icontains=project_name)
        return objs;



# mutation
class CreateTable(graphene.Mutation):
    company_name = graphene.String()
    contract_id = graphene.String()
    project_name = graphene.String()
    #project_id = graphene.String()
    #contract_project_name = graphene.String()
    #new_table_koujing = graphene.String()
    #construct_company = graphene.String()
    #project_group = graphene.String()
    #construct_person = graphene.String()
    #quality_person = graphene.String()
    #install_method = graphene.String()
    #table_id = graphene.String()
    #product_manager = graphene.String()
    #financial_check = graphene.String()
    #chairman_check = graphene.String()
    #project_deadline = graphene.DateTime() 
    #product_deadline = graphene.DateTime() 
    #quality_deadline = graphene.DateTime() 
    #compute_deadline = graphene.DateTime() 
    #plan_money = graphene.Float()
    #contract_money = graphene.Float()
    #money_get_previous = graphene.Float()
    #print_times = graphene.Int()
    #client_phone = graphene.Int()
    #client_address = graphene.String()
    #remark = graphene.String()

    class Arguments:
        company_name = graphene.String()
        contract_id = graphene.String()
        project_name = graphene.String()
        #project_id = graphene.String()
        #contract_project_name = graphene.String()
        #new_table_koujing = graphene.String()
        #construct_company = graphene.String()
        #project_group = graphene.String()
        #construct_person = graphene.String()
        #quality_person = graphene.String()
        #install_method = graphene.String()
        #table_id = graphene.String()
        #product_manager = graphene.String()
        #financial_check = graphene.String()
        #chairman_check = graphene.String()
        #project_deadline = graphene.DateTime() 
        #product_deadline = graphene.DateTime() 
        #quality_deadline = graphene.DateTime() 
        #compute_deadline = graphene.DateTime() 
        #plan_money = graphene.Float()
        #contract_money = graphene.Float()
        #money_get_previous = graphene.Float()
        #print_times = graphene.Int()
        #client_phone = graphene.Int()
        #client_address = graphene.String()
        #remark = graphene.String()

    def mutate(self, info, **kwargs):
        table = models.ProjectTable(
                company_name = kwargs['company_name'],
                contract_id = kwargs["contract_id"],
                project_name = kwargs["project_name"],
                #project_id = kwargs[""],
                #contract_project_name = kwargs[""],
                #new_table_koujing = kwargs[""],
                #construct_company = kwargs[""],
                #project_group = kwargs[""],
                #construct_person = kwargs[""],
                #quality_person = kwargs[""],
                #install_method = kwargs[""],
                #table_id = kwargs[""],
                #product_manager = kwargs[""],
                #financial_check = kwargs[""],
                #chairman_check = kwargs[""],
                #project_deadline = kwargs[""],
                #product_deadline = kwargs[""],
                #quality_deadline = kwargs[""],
                #compute_deadline = kwargs[""],
                #plan_money = kwargs[""],
                #contract_money = kwargs[""],
                #money_get_previous = kwargs[""],
                #print_times = kwargs[""],
                #client_phone = kwargs[""],
                #client_address = kwargs[""],
                #remark = kwargs[""],
            )
        table.save()
        return CreateTable(
            company_name = table.company_name,
            contract_id = table.contract_id,
            project_name = table.project_name,
        )

class Mutation(graphene.ObjectType):
    create_message = CreateMessage.Field()
    create_table = CreateTable.Field()
