from models import Hall, User, Lesson

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType


class HallType(SQLAlchemyObjectType):
    class Meta:
        model = Hall

class UserType(SQLAlchemyObjectType):
    class Meta:
        model = User

class LessonType(SQLAlchemyObjectType):
    class Meta:
        model = Lesson

class Query(graphene.ObjectType):
    get_all_lessons = graphene.List(LessonType)

    def resolve_get_all_lessons(self, info):
        query = LessonType.get_query(info)
        return query.all()


schema = graphene.Schema(query=Query)
