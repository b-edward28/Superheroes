from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin



metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'

    serialize_rules = ('-hero_powers.hero',) 

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)

    hero_powers = db.relationship('HeroPower', back_populates='hero', cascade='all, delete')


class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)

    hero_powers = db.relationship('HeroPower', back_populates='powers', cascade='all, delete')

    @validates('description')
    def validate_description(self, key, value):
        if not value or len(value) < 20:
            raise ValueError('Description must be at least 20 characters')
        return value

class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'hero_powers'

    serialize_rules = ('-hero.hero_powers', '-powers.hero_powers')

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)

    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))

    hero = db.relationship('Hero', back_populates='hero_powers')
    powers = db.relationship('Power', back_populates='hero_powers')

    @validates('strength')
    def validate_strength(self, key, value):
        allowed = ['Strong', 'Weak', 'Average']
        if value not in allowed:
            raise ValueError(f'Strength must be one of {allowed}')
        return value


