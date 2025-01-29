class BaseRepository:
    def __init__(self, session):
        self.session = session

    def create(self, model):
        self.session.add(model)
        self.session.commit()
        return model
