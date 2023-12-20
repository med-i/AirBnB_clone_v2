#!/usr/bin/python3
"""
Place Module for HBNB project
"""

from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from os import getenv


place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
    ),
)


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
        "Review",
        backref="place",
        cascade="all, delete-orphan",
    )

    amenities = relationship(
        "Amenity",
        secondary=place_amenity,
        back_populates="place_amenities",
        viewonly=False,
    )

    if getenv("HBNB_TYPE_STORAGE") != "db":
        amenity_ids = []

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

        @property
        def amenities(self):
            """amenities getter"""
            from models import storage

            all_amenities = storage.all(Amenity)
            return [
                amenity
                for amenity in all_amenities.values()
                if amenity.id in self.amenity_ids
            ]

        @amenities.setter
        def amenities(self, obj):
            """amenities setter"""
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
