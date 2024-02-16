from flask import Blueprint, render_template, request
from models.language_model import LanguageModel
from deep_translator import GoogleTranslator


translate_controller = Blueprint("translate_controller", __name__)


@translate_controller.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
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

    if request.method == "POST":
        _text = request.form.get("text-to-translate")
        _from = request.form.get("translate-from")
        _to = request.form.get("translate-to")
        _trans = GoogleTranslator(source=_from, target=_to).translate(_text)
        return render_template(
            "index.html",
            languages=LanguageModel.list_dicts(),
            text_to_translate=_text,
            translate_from=_from,
            translate_to=_to,
            translated=_trans,
        )


@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    _text = request.form.get("text-to-translate")
    _from = request.form.get("translate-from")
    _to = request.form.get("translate-to")
    _trans = GoogleTranslator(source=_from, target=_to).translate(_text)
    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        # inverte o text to translate
        text_to_translate=_trans,
        # inverte o from para to
        translate_from=_to,
        # inverte o to para from
        translate_to=_from,
        # inverte o translated
        translated=_text,
    )
