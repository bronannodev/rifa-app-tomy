from sqlalchemy import Column, Integer, Boolean, String, Float, DateTime
from datetime import datetime
from database import Base

class Numero(Base):
    __tablename__ = "numeros"

    numero = Column(Integer, primary_key=True, index=True)
    vendido = Column(Boolean, default=False, nullable=False)
    nombre = Column(String, nullable=True)
    referencia = Column(String, nullable=True)
    monto = Column(Float, nullable=True)
    metodo_pago = Column(String, nullable=True)
    fecha = Column(DateTime, nullable=True)