from .app.db import db
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import func
from datetime import datetime

class Bakery(db.Model,SerializerMixin):
    __tablename__="bakeries"

    id:Mapped[int]=mappped_column(primary_key=True)
    name:Mapped[str]
    created_at:Mapped[datetime]=mappped_column(server_default=func.now())
    updated_at:Mapped[datetime]=mapped_column(server_default=func.now(),onupdate=func.now())


    def __repr__(self):
        return f"<Bakery ({self.id}) {self.name}>"