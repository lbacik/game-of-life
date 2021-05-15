
from flask import Flask, jsonify, request
from flask_restx import Api, Resource, fields, reqparse

from game_of_life.cli.arguments import Arguments
from game_of_life.cli.cli import create_gol_arguments
from game_of_life.colony.colony import Colony
from game_of_life.colony.exception.colony_exception import ColonyException
from game_of_life.gol.factory import Factory

app = Flask(__name__)
api = Api(app=app, version="0.1")
name_space = api.namespace('', description='GoL Api')

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


class ColonyEntity:
    def __init__(self, colony: Colony, colony_id: str):
        self.colony = colony
        self.id = colony_id

    def json(self, page: int, limit: int):
        return {
            'id': self.id,
            'generations': len(self.colony._field_list),
            'status': self.colony._state,
            'history': [field._field for field in self.colony._field_list[(page-1)*limit:(page-1)+limit]],
            'history_page': page,
            'history_limit': limit
        }


colonies: dict = {}


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


get_parser = reqparse.RequestParser()
get_parser.add_argument('page', type=int, default=1)
get_parser.add_argument('limit', type=int, default=20)


@name_space.route('/colonies/', defaults={'colony_id': None})
@name_space.route('/colonies/<colony_id>')
class GameOfLifeApi(Resource):

    @name_space.expect(get_parser)
    def get(self, colony_id: str):
        if colony_id:
            args = get_parser.parse_args()
            result = {}
            colony = colonies[colony_id]
            if colony:
                result = colony.json(args['page'], args['limit'])
        else:
            result = [
                {
                    'id': colony_id,
                    'status': colonies[colony_id].colony._state,
                    'generations': len(colonies[colony_id].colony._field_list)
                } for colony_id in colonies.keys()
            ]
        return jsonify(result)

    @name_space.expect(model_colony, validate=True)
    def post(self, colony_id=None):
        app.logger.debug(api.payload)

        # async
        colony = process_colony(api.payload)
        if colony_id is None:
            colony_id = hash(colony)
        colonies[str(colony_id)] = ColonyEntity(colony, colony_id)

        # only colony id (async)
        return jsonify({
            'id': colony_id,
            'generations': len(colony._field_list),
            'status': colony._state
        })


app.run(port=8080)
