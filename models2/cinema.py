from sqlalchemy import Column, Integer, String

from models2.database import Base


class Сinema(Base):
    __tablename__ = 'cinema'

    id = Column(Integer, primary_key=True)
    country = Column(String(250), nullable=False)
    town = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    number = Column(String(250), nullable=False)
    rating_cinema = Column(Integer)

    def __init__(self, country, town, name, number, rating_cinema):
        self.country = country
        self.town = town
        self.name = name
        self.number = number
        self.rating_cinema = rating_cinema

    def __repr__(self):
        return f"Кинотеатр (Страна: {self.country}, Город: {self.town}, Название: {self.name}, " \
               f"Номер телефона: {self.number}, Рейтинг кинотеатра: {self.rating_cinema})"
