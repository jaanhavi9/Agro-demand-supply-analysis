from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app_fastapi = FastAPI()

class CommodityInput(BaseModel):
    commodity_name: str
    num_days: int

@app_fastapi.post('/predict_prices')
def predict_prices(data: CommodityInput):

    predicted_prices = {"predicted_prices": [50, 55, 60]}  

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app_fastapi, host="localhost", port=8000)
