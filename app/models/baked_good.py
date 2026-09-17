from app.db import db
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import func,ForeignKey
from datetime import datetime

class BakedGood(db.Model,SerializerMixin):
    __tablename__="baked_goods"

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]
    price:Mapped[int]
    created_at:Mapped[datetime]=mapped_column(server_default=func.now())
    updated_at:Mapped[datetime]=mapped_column(server_default=func.now(),onupdate=func.now())

    bakery_id:Mapped[int]=mapped_column(ForeignKey("bakeries.id"))

    bakery:Mapped["Bakery"]=relationship(back_populates="baked_goods")

    def __repr__(self):
        return f"<BakedGood ({self.id}) {self.name}, {self.price}>"