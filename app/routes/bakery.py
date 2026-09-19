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
@bakery_bp.route('/<int:id>')
def bakery_by_id(id):
    bakery=Bakery.query.filter(Bakery.id == id).first()

    if bakery is None:
        response_body={
            "message":"The record does not exist in our database!!!!"
        }
        return make_response(response_body,404)

    bakery_dict=bakery.to_dict(rules=("-baked_goods",))

    response=make_response(
        bakery_dict,
        200
    )
    return response