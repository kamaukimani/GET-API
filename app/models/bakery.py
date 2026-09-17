from app.db import db
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import func
from datetime import datetime
from typing import List

class Bakery(db.Model,SerializerMixin):
    __tablename__="bakeries"

    serialize_rules=("-baked_goods.bakery",)

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]
    created_at:Mapped[datetime]=mapped_column(server_default=func.now())
    updated_at:Mapped[datetime]=mapped_column(server_default=func.now(),onupdate=func.now())

    baked_goods:Mapped[List["BakedGood"]]=relationship(back_populates="bakery",cascade="all,delete-orphan")

    def __repr__(self):
        return f"<Bakery ({self.id}) {self.name}>"