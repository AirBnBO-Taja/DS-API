from fastapi import APIRouter

router = APIRouter()

@router.get('/db')
async def update_db():
    return {'placeholder': 'to do'}