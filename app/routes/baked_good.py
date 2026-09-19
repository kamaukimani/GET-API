from flask import Blueprint,request,make_response
from app.models import BakedGood
from app.db import db

baked_good_bp=Blueprint("baked_good",__name__)

@baked_good_bp.route("/all",methods=["GET","POST"])
def baked_goods():
    if request.method == "GET":
        baked_goods=[]

        for baked_good in BakedGood.query.all():
            baked_good_dict=baked_good.to_dict(rules=("-bakery",))
            baked_goods.append(baked_good_dict)

        response=make_response(
            baked_goods,
            200
        )
        return response
    elif request.method == "POST":
        data=request.get_json()
        name=data["name"]
        price=data["price"]
        bakery_id=data.get("bakery_id")

        new_baked_good=BakedGood(
            name=name,
            price=price,
            bakery_id=bakery_id
        )
        db.session.add(new_baked_good)
        db.session.commit()

        baked_good_dict=new_baked_good.to_dict()
        response=make_response(
            baked_good_dict,
            201
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
@baked_good_bp.route('/<int:id>')
def find_by_id(id):
    baked_good=BakedGood.query.filter(BakedGood.id == id).first()

    if baked_good is None:
        return {
            "message":"The record does not exist in our database!!!"
        },200
    baked_good_dict=baked_good.to_dict()
    response=make_response(
        baked_good_dict,
        200
    )
    return response