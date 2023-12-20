#!/usr/bin/python3
"""
State Module for HBNB project
"""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """
    This class defines an amenity
    """

    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)

    place_amenities = relationship(
        "Place",
        secondary="place_amenity",
        back_populates="amenities",
        viewonly=False,
    )
