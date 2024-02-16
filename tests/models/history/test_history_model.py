import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    history_json = HistoryModel.list_as_json()
    assert json.loads(history_json)[0]["translate_to"] == "pt"
    assert json.loads(history_json)[0]["translate_from"] == "en"
    assert json.loads(
        history_json
        )[0]["text_to_translate"] == "Hello, I like videogame"
