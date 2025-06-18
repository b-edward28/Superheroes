from flask import Flask, request, make_response
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

#GET
@app.route('/')
def index():
    return '<h1>Superheroes</h1>'

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    heroes_list = [hero.to_dict(rules=('-hero-powers',)) for hero in heroes]

    return make_response(heroes_list, 200)

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    powers_list = [power.to_dict(rules=('-hero_powers',)) for power in powers]

    return make_response(powers_list, 200)


#Get by ID
@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return make_response({'error': 'Hero not found'}, 404)
    hero_dict = hero.to_dict(rules=('-hero-powers', 'hero_powers.power'))
    return make_response(hero_dict, 200)

@app.route('/powers/<int:id>', methods=['GET'])
def get_power_by_id(id):
    power = Power.query.get(id)
    if not power:
        return make_response({'error': 'Power not found'}, 404)
    power_dict = power.to_dict(rules=('-hero_powers', 'hero_powers.hero'))
    return make_response(power_dict, 200)

#PATCH
@app.route('/heroes/<int:id>', methods=['PATCH'])
def update_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return make_response({'error': 'Hero not found'}, 404)

    data = request.get_json()

    if 'name' in data:
        try:
            hero.name = data['name']
        except ValueError as e:
            return make_response({'error': str(e)}, 400)

    if 'super_name' in data:
        try:
            hero.super_name = data['super_name']
        except ValueError as e:
            return make_response({'error': str(e)}, 400)

    db.session.commit()
    return make_response(hero.to_dict(rules=('-hero-powers',)), 200)

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return make_response({'error': 'Power not found'}, 404)

    data = request.get_json()
    if 'description' in data:
        try:
            power.description = data['description']
        except ValueError as e:
            return make_response({'error': str(e)}, 400)

    db.session.commit()
    return make_response(power.to_dict(rules=('-hero_powers',)), 200)


#POST
@app.route('/hero_powers', methods=['POST'])
def add_hero_power():
    data = request.get_json()

    try:
        strength = data['strength']
        power_id = data['power_id']
        hero_id = data['hero_id']

        if not all([strength, power_id, hero_id]):
            raise ValueError('All fields are required')
        
        new_hero_power = HeroPower(
            strength=strength,
            power_id=power_id,
            hero_id=hero_id
        )
        db.session.add(new_hero_power)
        db.session.commit()

        response_data = {
            'id': new_hero_power.id,
            'strength': new_hero_power.strength,
            'power_id': new_hero_power.power_id,
            'hero_id': new_hero_power.hero_id,
            'hero': {
                'id': new_hero_power.hero.id,
                'name': new_hero_power.hero.name,
                'super_name': new_hero_power.hero.super_name
            },
            'power': {
                'id': new_hero_power.power.id,
                'name': new_hero_power.power.name,
                'description': new_hero_power.power.description
            }
        }
        return make_response(response_data, 201)
    except ValueError as ve:
        return make_response({'error': str(ve)}, 400)
    except Exception as e:
        return make_response({'error': str(e)}, 500)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
