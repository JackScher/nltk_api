import nltk
from flask import Blueprint, jsonify, request, Response
from api import log
from api.logger import log
from api.schema import BaseSchema, ResponseSchema


nltk_blueprint = Blueprint("nltk", __name__, url_prefix="/")


@nltk_blueprint.route("/tokenize", methods=["POST"])
def tokenize() -> Response:
        log(log.INFO, "Tokenize starting")
        if not request.is_json:
            log(log.ERROR, "Unsupported Media Type")
            return jsonify(BaseSchema(status="error", message="Content-Type must be application/json").model_dump()), 415
        
        data = request.get_json()
        if "text" not in data:
            log(log.ERROR, "No text received")
            return jsonify(BaseSchema(status="error", message="No text received").model_dump()), 400
        
        text = data.get("text")
        tokens = nltk.word_tokenize(text)
        log(log.INFO, "Successful tokenize")
        return jsonify(ResponseSchema(status="success", message="Text tokenized", data=tokens).model_dump()), 200


@nltk_blueprint.route("/post_tag", methods=["POST"])
def post_tag() -> Response:
        log(log.INFO, "Post_tag starting")
        if not request.is_json:
            log(log.ERROR, "Unsupported Media Type")
            return jsonify(BaseSchema(status="error", message="Content-Type must be application/json").model_dump()), 415
        
        data = request.get_json()
        if "text" not in data:
            log(log.ERROR, "No text received")
            return jsonify(BaseSchema(status="error", message="No text received").model_dump()), 400
        
        text = data.get("text")
        tokens = nltk.word_tokenize(text)
        tags = nltk.pos_tag(tokens)
        log(log.INFO, "Successful post_tag")
        return jsonify(ResponseSchema(status="success", message="Partial language markup got", data=tags).model_dump()), 200


@nltk_blueprint.route("/ner", methods=["POST"])
def ner() -> Response:
        log(log.INFO, "Ner starting")
        if not request.is_json:
            log(log.ERROR, "Unsupported Media Type")
            return jsonify(BaseSchema(status="error", message="Content-Type must be application/json").model_dump()), 415
        
        data = request.get_json()
        if "text" not in data:
            log(log.ERROR, "No text received")
            return jsonify(BaseSchema(status="error", message="No text received").model_dump()), 400
        
        text = data.get("text")
        tokens = nltk.word_tokenize(text)
        tags = nltk.pos_tag(tokens)
        named_entities = nltk.ne_chunk(tags)

        entities = []
        for entity in named_entities:
            if isinstance(entity, nltk.tree.Tree):
                entities.append((' '.join([word for word, tag in entity]), entity.label()))

        log(log.INFO, "Successful ner")
        return jsonify(ResponseSchema(status="success", message="Recognition of named entities done", data=entities).model_dump()), 200
