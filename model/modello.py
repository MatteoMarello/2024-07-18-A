from database.DAO import DAO


class Model:
    def __init__(self):
        pass
    def getCromosomiModel(self):
        return DAO.get_cromosomi()
