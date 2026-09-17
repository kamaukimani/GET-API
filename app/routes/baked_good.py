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
