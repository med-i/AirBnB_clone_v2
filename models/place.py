#!/usr/bin/python3
"""
Place Module for HBNB project
"""

from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Place(BaseModel, Base):
    """
    A place to stay
    """

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    reviews = relationship(
        "Review", backref="place", cascade="all, delete-orphan"
    )

    @property
    def reviews(self):
        """Returns the list of Review instances with
        place_id equals to the current Place.id"""
        from models import storage
        from models.review import Review

        all_reviews = storage.all(Review)
        return [
            review
            for review in all_reviews.values()
            if review.place_id == self.id
        ]
