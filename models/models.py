from sqlalchemy import Column, Float, ForeignKey, Integer, MetaData, String
from sqlalchemy.orm import DeclarativeBase, relationship

metadata = MetaData()


class Base(DeclarativeBase):
    pass


class Menus(Base):
    __tablename__ = 'menus'
    metadata = metadata
    id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )

    title = Column(String(250), nullable=False)
    description = Column(String, nullable=False)

    submenus = relationship('Submenus', back_populates='menus')


class Submenus(Base):
    __tablename__ = 'submenus'
    metadata = metadata
    id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )

    title = Column(String(250), nullable=False)
    description = Column(String, nullable=False)

    menu_id = Column(
        Integer,
        ForeignKey('menus.id', ondelete='CASCADE'),
        nullable=False
    )
    menu = relationship('Menus', back_populates='submenus')

    dishes = relationship('Dishes', back_populates='submenus')


class Dishes(Base):
    __tablename__ = 'dishes'
    metadata = metadata
    id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )

    title = Column(String(250), nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    submenu_id = Column(
        Integer,
        ForeignKey('submenus.id', ondelete='CASCADE'),
        nullable=False
    )
    submenu = relationship('Submenus', back_populates='dishes')
