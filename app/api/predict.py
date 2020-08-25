import logging
import random

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator

log = logging.getLogger(__name__)
router = APIRouter()


class Hottel(BaseModel):
    """Use this data model to parse the request body JSON."""
    accommodates: int
    bathrooms: int
    bedrooms: float
    beds: int
    guest_included: bool
    minimum_night: int
    maximum_night: int 

    def to_df(self):
        return pd.DataFrame([dict(self)])
    
@router.post('/predict')
async def predict(hottel: Hottel):
    """
    Predict the price of hottel
    """
    x_new = hottel.to_df()
    y_pred = 300
    return {
        'predicted_price': y_pred
    }
