from typing import List

import joblib
import requests
import numpy as np

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse


app = FastAPI()


@app.get("/api/recommendations/{product_id}")
def get_recommendations(product_id: int) -> JSONResponse:
    nbrs = joblib.load('knn.joblib')
    product = requests.get(f'http://86.107.197.218:15800/api/product/{product_id}').json()

    distances, indices = nbrs.kneighbors(
        np.array([[product['category']['id'], product['price'], product['brand']['id']]]))

    indices = indices.flatten().tolist()

    products = list()
    for index in indices:
        recommended_products = requests.get(f'http://86.107.197.218:15800/api/product/{index}').json()
        products.append(recommended_products)

    return JSONResponse({"products": products})
