from faker import Faker

from models2.database import create_db, Session
from models2.cinema import Сinema


def create_database2(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):

    faker = Faker('ru_RU')
    session.commit()

    group_list = ['Имаджинариум', 'Пять звезд', 'Мега Ролан', 'Синема Парк', 'Премьер зал',
                  'Художественный кинотеатр', 'Формула кино', 'Фабрика Грез', 'Мадагаскар']

    for _ in range(10):
        country = faker.country()
        town = faker.city()
        name = faker.random.choice(group_list)
        number = faker.phone_number()
        rating_cinema = faker.random.randint(1, 11)
        cinema = Сinema(country, town, name, number, rating_cinema)
        session.add(cinema)

    session.commit()
    session.close()
