from sqlalchemy.orm import Session
from fastapi import Depends
from services.point_import import PointImportService
from db.postgres import get_db




def get_point_import_service(
    db: Session = Depends(get_db),
):
    return PointImportService(db)
