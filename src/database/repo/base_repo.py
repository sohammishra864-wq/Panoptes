from typing import List, TypeVar, Generic, Optional
from sqlalchemy.orm import Session
from sqlalchmey import delete ,select
from src.database.base import Base

ModelType = TypeVar('ModelType',bound=Base) # well each will inherit using super
# modeltype is any model that inherit using the base , base maps it to db table using session

class BaseRepo(Generic[ModelType]):
    def __init__(self,session: Session , model: type[ModelType]):
        self.session = session
        self.model = model

    def get_by_id(self,id:str) -> Optional[ModelType] : # id will be pk
        return self.session.get(self.model,id)

    def create(self,obj: ModelType) -> ModelType:  # basic crud
        self.session.add(self.model)
        self.session.flush()
        return obj

    def update(self,obj: ModelType) -> ModelType:
        self.session.merge(obj)
        self.session.flush()
        return obj

    def delete(self,obj: ModelType) -> ModelType:
        obj = self.get_by_id(obj.id)
        if obj is None:
            return False
        self.session.delete(obj)
        self.session.flush()
        return True
