
from .arguments import parse, Arguments
from ..game_of_life.arguments import Arguments as GolArguments
from .start_field.only_string import input_field as field_from_string
from .start_field.string_with_width import input_field as field_from_string_with_width
from .start_field.from_file import input_field as field_from_file
from ..game_of_life.factory import Factory
from ..game_of_life.field import Field


def create_gol_arguments(args: object) -> GolArguments:
    if args.file_start_generation:
        field = field_from_file(args.file_start_generation, args.file_false, args.file_true)
    elif (args.width > 0):
        field = field_from_string_with_width(args.start_generation, args.width)
    else:
        field = field_from_string(args.start_generation)

    width: int = field.width()
    start_generation: str = field.__str__()

    return GolArguments(start_generation, width)


def show_generation(generation: Field) -> None:
    for point in generation:
        value = generation.state_point(point)
        if value:
            # char = chr(9634)
            # char = ' ' + chr(9632)
            char = 'O '
        else:
            # char = chr(1468) + ' '
            char = '. '
        if point.x == generation.geometry().x - 1:
            print(char)
        else:
            print(char, end='')


args = parse()

gol_arguments = create_gol_arguments(args)
gol = Factory.create_from_arguments(gol_arguments)

for i in range(0, args.generations + 1):

    print(f" >> gen: {i}")
    show_generation(gol.field())
    print(' = = =')

    input("Press Enter to continue...")

    if i < args.generations:
        gol.next_generation()
