from flask import Blueprint,request,make_response
from app.models import BakedGood

baked_good_bp=Blueprint("baked_good",__name__)

@baked_good_bp.route("/all")
def baked_goods():
    baked_goods=[]

    for baked_good in BakedGood.query.all():
        baked_good_dict=baked_good.to_dict(rules=("-bakery",))
        baked_goods.append(baked_good_dict)

    response=make_response(
        baked_goods,
        200
    )
    return response

@baked_good_bp.route('/by_price')
def baked_goods_by_price():
    baked_goods=[]
    for baked_good in BakedGood.query.order_by(BakedGood.price.desc()).all():
        baked_good_dict=baked_good.to_dict(rules=("-bakery",))
        baked_goods.append(baked_good_dict)
    response=make_response(
        baked_goods,
        200
    )
    return response
@baked_good_bp.route('/most_expensive')
def most_expensive_baked_good():
    baked_good=BakedGood.query.order_by(BakedGood.price.desc()).first()
    #baked_good=BakedGood.query.order_by(BakedGood.price.desc()).limit(1).all() ==> return a list
    #you have to loop through it
    baked_good_dict=baked_good.to_dict(rules=("-bakery",))

    response=make_response(
        baked_good_dict,
        200
    )
    return response
