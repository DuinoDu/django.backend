import graphene
from graphene_django.types import DjangoObjectType

from . import models


class MessageType(DjangoObjectType):
    class Meta:
        model = models.Message
        interfaces = (graphene.Node, )


class Query(graphene.AbstractType):
    all_messages = graphene.List(MessageType)
    message = graphene.Field(MessageType, id=graphene.ID())

    def resolve_all_messages(self, args, **kwargs): #context, info):
        return models.Message.objects.all()
