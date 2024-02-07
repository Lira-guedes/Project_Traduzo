from database.db import db
from models.abstract_model import AbstractModel


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data: dict):
        super().__init__(data)

    # cria um novo dicionário contendo os valores dos atributos name e acronym
    # que será retornado como resultado da função
    def to_dict(self) -> dict:
        return {
            "name": self.data.get("name"),
            "acronym": self.data.get("acronym")
        }

    # retorna uma lista de dicionários com todas as language no banco
    @classmethod
    def list_dicts(cls) -> list:
        # itera sobre todas as languages da _collection retornadas pelo find()
        # para cada language, cria uma instância de LanguageModel e chama
        # o to_dict() para converter em um dicionário
        # e os adiciona à lista de idiomas
        return [cls(language).to_dict() for language in cls._collection.find()]
