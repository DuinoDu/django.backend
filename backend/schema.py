import graphene

import simple_app.schema

class Query(
        simple_app.schema.Query, 
        graphene.ObjectType):
    pass

#class Mutation(
#        simple_app.schema.Mutation, 
#        graphene.ObjectType):
#    pass

schema = graphene.Schema(query=Query) #, mutation=Mutation)
