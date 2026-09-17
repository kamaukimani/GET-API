
from random import choice as rc

from app import create_app
from app.db import db
from app.models import Bakery, BakedGood

app=create_app()
with app.app_context():

    BakedGood.query.delete()
    Bakery.query.delete()
    
    bakeries = []
    bakeries.append(Bakery(name='Delightful donuts'))
    bakeries.append(Bakery(name='Incredible crullers'))
    db.session.add_all(bakeries)

    baked_goods = []
    baked_goods.append(BakedGood(name='Chocolate dipped donut', price=2.75, bakery=bakeries[0]))
    baked_goods.append(BakedGood(name='Apple-spice filled donut', price=3.50, bakery=bakeries[0]))
    baked_goods.append(BakedGood(name='Glazed honey cruller', price=3.25, bakery=bakeries[1]))
    baked_goods.append(BakedGood(name='Chocolate cruller', price=3.40, bakery=bakeries[1]))

    db.session.add_all(baked_goods)
    db.session.commit()