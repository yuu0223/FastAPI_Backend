from fastapi import APIRouter
from sqlalchemy.orm.session import Session
from fastapi.params import Depends
from utils.db_conn import get_db
from services.medical import business

router = APIRouter(prefix="/medical", tags=["medical"])

@router.get("/medical_articles", summary="醫療文章內容")
async def get_medical_info(medical_id:int,db: Session = Depends(get_db)):

    return await business.get_medical_data(medical_id,db) #test