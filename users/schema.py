#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : schema.py
# Author            : duino <472365351duino@gmail.com>
# Date              : 15.07.2018
# Last Modified Date: 17.07.2018
# Last Modified By  : du min <min.du@hobot.cc>
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

import graphene
from graphene_django import DjangoObjectType

from .invitation import Alist, Blist, Clist

Agroup = Group.objects.get(name='A')
Bgroup = Group.objects.get(name='B')
Cgroup = Group.objects.get(name='C')


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    permissions = graphene.Field(graphene.String, username=graphene.String())

    def resolve_users(self, info):
        return get_user_model().objects.all()

    def resolve_permissions(self, info, username):
        user = get_user_model().objects.filter(username=username)[0]
        return list(user.get_group_permissions())[0]


### Error Message


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    msg = graphene.Field(graphene.String)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        invitation = graphene.String(required=True)

    def mutate(self, info, username, password, invitation): 
        msg = "";
        if get_user_model().objects.filter(username=username).exists():
            msg = "001 Username already exists"
            return CreateUser(user=None, msg=msg)
        try:
            user = get_user_model()(username=username)
        except Exception as e:
            msg = "002 Something went wrong"
            return CreateUser(user=None, msg=msg)
        user.save() # only to set id

        # set group based on invitation
        if invitation in Alist:
            user.groups.add(Agroup)
        elif invitation in Blist:
            Bgroup.user_set.add(user)
        elif invitation in Clist:
            Cgroup.user_set.add(user)
        else:
            msg = "003 Invalid invitation code",
            user.delete()
            return CreateUser(user=None, msg=msg)

        user.set_password(password)
        user.save()
        msg = "000 Create user successfully"
        return CreateUser(user=user, msg=msg)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
