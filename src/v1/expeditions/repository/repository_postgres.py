from src.v1.expeditions.repository.repository import ExpeditionsRepository
from src.v1.model.expeditions import expeditions


class ExpeditionsRepositoryPSQL(ExpeditionsRepository):
    def __init__(self, db):
        self._db = db
        super(ExpeditionsRepositoryPSQL, self).__init__()
    
    def get(self, read=True):
        self.current_db = self.db.get('read')

    async def get_all(self, filters):
        query = expeditions.select()
        try:
            data = await self.db('read').fetch_all(query)
        except Exception as e:
            print(e, "error ")
            data = e

        return data

    async def get_by_id(self, id):
        query = expeditions.select().where('id' == id)
        try:
            data = await self.db('read').fetch_one(query)
        except Exception as e:
            data = e

        return data