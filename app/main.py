from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api import predict, viz, db 

app = FastAPI(
    title='Hottel Booking DS API',
    description='Hotel booking and the price comparisson',
    version='0.1',
    docs_url='/',
)

app.include_router(predict.router)
app.include_router(viz.router)
app.include_router(db.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)
