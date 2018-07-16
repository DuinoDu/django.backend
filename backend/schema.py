#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : backend/schema.py
# Author            : duino <472365351duino@gmail.com>
# Date              : 15.07.2018
# Last Modified Date: 15.07.2018
# Last Modified By  : duino <472365351duino@gmail.com>
import graphene
import graphql_jwt

import simple_app.schema
import users.schema

class Query(
        simple_app.schema.Query, 
        users.schema.Query, 
        graphene.ObjectType):
    pass

class Mutation(
        simple_app.schema.Mutation, 
        users.schema.Mutation,
        graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
