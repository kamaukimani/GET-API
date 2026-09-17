from flask import Blueprint,request,make_response
from app.models import Bakery
bakery_bp=Blueprint("bakery",__name__)

@bakery_bp.route('/all')
def bakeries():
    bakeries=[]
    for bakery in Bakery.query.all():
        bakery_dict=bakery.to_dict(rules=("-baked_goods",))
        bakeries.append(bakery_dict)
    response=make_response(
        bakeries,
        200
    )
    return response