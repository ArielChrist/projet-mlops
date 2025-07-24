from pydantic import BaseModel

class features(BaseModel):
      date: str
      bedrooms: float
      bathrooms: float
      sqft_living: float
      sqft_lot: float
      floors: float
      waterfront: int
      view: int
      condition: int
      sqft_above: float
      sqft_basement: float
      yr_built: int
      yr_renovated: int
      street: str
      city: str
      statezip: str
      country: str 

class Target(BaseModel):
    price: float
