from flask import Blueprint, render_template
from models.language_model import LanguageModel


translate_controller = Blueprint("translate_controller", __name__)


@translate_controller.route("/", methods=["GET"])
def index():
    # renderiza o template e passa as variaveis pra ele
    return render_template(
        "index.html",
        # obtem todos os idiomas disponiveis usando
        # o método list_dicts() do LanguageModel
        languages=LanguageModel.list_dicts(),
        # define as variaveis para enviar para o template
        text_to_translate="O que deseja traduzir?",
        translate_from="pt",
        translate_to="en",
        translated="What do you want to translate?",
    )
