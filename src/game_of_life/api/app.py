from flask import Flask, jsonify
from flask_restx import Api, Resource, fields

from game_of_life.cli.arguments import Arguments
from game_of_life.cli.cli import create_gol_arguments
from game_of_life.colony.colony import Colony
from game_of_life.colony.exception.colony_exception import ColonyException
from game_of_life.gol.factory import Factory

app = Flask(__name__)
api = Api(app=app, version="0.1")
name_space = api.namespace('Game of Life', description='GoL Api')

RESULT_TYPE_GENERATION_NUMBER = 'GEN_NUMBER'

MODEL_WIDTH = 'width'
MODEL_START_GENERATION = 'start'
MODEL_NUMBER_OF_GENERATIONS = 'generations'
MODEL_RESULT_TYPE = 'result'

model_colony = api.model('Colony', {
    MODEL_WIDTH: fields.Integer(),
    MODEL_START_GENERATION: fields.String,
    MODEL_NUMBER_OF_GENERATIONS: fields.Integer(default=1),
    MODEL_RESULT_TYPE: fields.String(default=RESULT_TYPE_GENERATION_NUMBER),
})


def process_colony(payload) -> Colony:
    args = Arguments()
    args.start_generation = payload[MODEL_START_GENERATION]
    args.width = payload[MODEL_WIDTH]
    gol_arguments = create_gol_arguments(args)
    gol = Factory.create_from_arguments(gol_arguments)
    colony = Colony(gol)
    try:
        for i in range(0, payload[MODEL_NUMBER_OF_GENERATIONS]):
            colony.next_generation()
    except ColonyException as exception:
        pass

    return colony


@name_space.route("/")
class GameOfLifeApi(Resource):

    @staticmethod
    @name_space.expect(model_colony)
    def post():
        app.logger.debug(api.payload)
        colony = process_colony(api.payload)
        return jsonify({
            'generations': len(colony._field_list) - 1,
            'status': colony._state
        })


app.run(port=8080)
