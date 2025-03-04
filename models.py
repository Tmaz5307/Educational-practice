from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
Base = declarative_base()


class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True)
    номер_комнаты = Column(String, nullable=False)
    вместимость = Column(Integer, nullable=False)

    residents = relationship('Resident', back_populates='room')


class Resident(Base):
    __tablename__ = 'residents'

    id = Column(Integer, primary_key=True)
    имя = Column(String, nullable=False)
    возраст = Column(Integer, nullable=False)
    комната_id = Column(Integer, ForeignKey('rooms.id'))

    room = relationship('Room', back_populates='residents')


# Создаем базу данных SQLite
engine = create_engine('sqlite:///hostel0.db')
Base.metadata.create_all(engine)
