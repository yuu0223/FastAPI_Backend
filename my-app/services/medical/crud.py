from utils.db_model import MedicalArticles
from sqlalchemy.orm.session import Session


async def get_medical_list(medical_id: int, db: Session):
    medical_articles = [
        {
            "ID": data[0],
            "title": data[1],
            "author": data[2],
            "article": data[3],
            "url": data[4],
        }
        for data in db.query(
            MedicalArticles.ID,
            MedicalArticles.Title,
            MedicalArticles.Author,
            MedicalArticles.Article,
            MedicalArticles.Url,
        )
        .filter(MedicalArticles.ID > medical_id)
        .limit(5)
        .all()
    ]

    if medical_articles:
        return medical_articles
    else:
        return []
