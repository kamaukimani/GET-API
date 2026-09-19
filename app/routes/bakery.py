from flask import Blueprint,request,make_response
from app.models import Bakery
from app.db import db
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
@bakery_bp.route('/<int:id>',methods=["GET","PATCH","DELETE","PUT","POST"])
def bakery_by_id(id):
    bakery=Bakery.query.filter(Bakery.id == id).first()

    if bakery is None:
        response_body={
            "message":"The record does not exist in our database!!!!"
        }
        return make_response(response_body,404)

    if request.method == "GET":
        bakery_dict=bakery.to_dict(rules=("-baked_goods",))

        response=make_response(
            bakery_dict,
            200
        )
        return response
    elif request.method == "PATCH":
        data=request.get_json()

        for attr,value in data.items():
            setattr(bakery,attr,value)
        db.session.add(bakery)
        db.session.commit()

        bakery_dict=bakery.to_dict(rules=("-baked_goods",))
        response=make_response(
            bakery_dict,
            200
        )
        return response
    else:
        return {"message":f"{request.method} does not exist yet"},405