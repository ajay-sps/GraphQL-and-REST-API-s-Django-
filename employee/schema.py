import graphene
from graphene_django import DjangoObjectType
from graphene import InputObjectType, Mutation
from graphene import String, Int, Boolean
from employee.models  import Department,Employee



class DepartmentType(DjangoObjectType):
    class Meta:
        model = Department
        fields = ['id','name']

    
class DepartmentInputType(InputObjectType):
    name = String()


class CreateDepartment(Mutation):
    class Arguments:
        input = DepartmentInputType()

    status = Boolean()
    department = graphene.Field(DepartmentType)

    @staticmethod
    def mutate(root, info, input):
        print(input)
        department = Department(name=input.name)
        department.save()
        return CreateDepartment(status=201, department=department)



class Query(graphene.ObjectType):
    # Define your query fields here
    all_departments = graphene.List(DepartmentType)

    def resolve_all_departments(self, info):
        # Define how to resolve the query for all departments
        return Department.objects.all()
    

class Mutation(graphene.ObjectType):
    create_department = CreateDepartment.Field()



schema = graphene.Schema(query=Query,mutation=Mutation)