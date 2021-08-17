from typing import Any, List, Optional

from pydantic import BaseModel
from regression_model.processing.validation import CarDataInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[float]]


class MultipleCarDataInputs(BaseModel):
    inputs: List[CarDataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "Name": "MARUTI VITARA BREZZA ZDI PLUS",
                        "Location": "Kochi",
                        "Year": "2018",
                        "Kilometers_Driven": 57078,
                        "Fuel_Type": "Diesel",
                        "Transmission": "Manual",
                        "Owner_Type": "First",
                        "Mileage": "24.3 kmpl",
                        "Engine": "1248 CC",
                        "Power": "88.5 bhp",
                        "Seats": 5.0,
                        "New_Price": "11.58 Lakh",
                    }
                ]
            }
        }
