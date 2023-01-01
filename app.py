from schemas import schema
from models import Base, engine, db_session, Hall, User, Lesson

from aiohttp import web
from aiohttp_graphql import GraphQLView
from sqlalchemy_utils import database_exists, create_database


# Create DB if not exists and populate with dummy data
async def on_startup(app):
    if not database_exists(engine.url):
        create_database(engine.url)

    Base.metadata.create_all(engine) # Will not recreate already present tables

    new_hall = Hall(city='Kyiv', street='Velyka Vasylkivska, 22')
    db_session.add(new_hall)

    new_user = User(name='Alina')
    db_session.add(new_user)

    new_lesson = Lesson(hall=new_hall, coach=new_user)
    db_session.add(new_lesson)

    db_session.commit()
    db_session.close()


async def on_shutdown(app):
    db_session.remove()


if __name__ == '__main__':
    app = web.Application()
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    GraphQLView.attach(app, schema=schema, graphiql=True)

    web.run_app(app)
