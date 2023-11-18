from enum import Enum


class Property(Enum):
    BLACK = 'black'
    RED = 'red'
    GREEN = 'green'
    YELLOW = 'yellow'
    BLUE = 'blue'
    MAGENTA = 'magenta'
    CYAN = 'cyan'
    WHITE = 'white'

    BG_BLACK = 'bgblack'
    BG_RED = 'bgred'
    BG_GREEN = 'bggreen'
    BG_YELLOW = 'bgyellow'
    BG_BLUE = 'bgblue'
    BG_MAGENTA = 'bgmagenta'
    BG_CYAN = 'bgcyan'
    BG_WHITE = 'bgwhite'

    BOLD = 'bold'
    UNDERLINE = 'underline'
    ITALIC = 'italic'
    BLINK = 'blink'
    INVERT = 'invert'
    CONCEAL = 'conceal'
    STRIKE = 'strike'


class Console:
    @staticmethod
    def print(input_data):
        """Takes in a list of dictionaries where each dictionary has a 'word', 'properties', 'spaces', and prints it
        to the console"""
        for data in input_data:
            word = data.get('word', '')
            properties = [prop.lower() for prop in data.get('properties', [])]
            spaces = data.get('spaces', 0)
            Console.print_word(word, properties, spaces)

    @staticmethod
    def print_word(word, properties, spaces):
        """Takes in a word, a list of properties, and the number of spaces, and prints the word with the properties
        and spaces"""

        # Loop through the properties and print the word with the properties
        output = ''
        for prop in properties:
            # Add ANSI escape codes based on the property
            output += Console.get_property_code(prop)

        # Print the word with the properties
        print(f"{output}{word}\033[0m", end='')

        # Print spaces with the same attributes as the word
        for _ in range(spaces):
            print(f"{output} \033[0m", end='')

    @staticmethod
    def get_property_code(prop):
        """Returns the ANSI escape code for a given property"""
        property_codes = {
            Property.BLACK.value: '\033[30m',
            Property.RED.value: '\033[31m',
            Property.GREEN.value: '\033[32m',
            Property.YELLOW.value: '\033[33m',
            Property.BLUE.value: '\033[34m',
            Property.MAGENTA.value: '\033[35m',
            Property.CYAN.value: '\033[36m',
            Property.WHITE.value: '\033[37m',

            Property.BG_BLACK.value: '\033[40m',
            Property.BG_RED.value: '\033[41m',
            Property.BG_GREEN.value: '\033[42m',
            Property.BG_YELLOW.value: '\033[43m',
            Property.BG_BLUE.value: '\033[44m',
            Property.BG_MAGENTA.value: '\033[45m',
            Property.BG_CYAN.value: '\033[46m',
            Property.BG_WHITE.value: '\033[47m',

            Property.BOLD.value: '\033[1m',
            Property.UNDERLINE.value: '\033[4m',
            Property.ITALIC.value: '\033[3m',
            Property.BLINK.value: '\033[5m',
            Property.INVERT.value: '\033[7m',
            Property.CONCEAL.value: '\033[8m',
            Property.STRIKE.value: '\033[9m',
        }

        return property_codes.get(prop, '')


# Example 1:
if __name__ == '__main__':
    data_to_print = [
        {"word": "Hello", "properties": ["bold", "underline", "bgblue"], "spaces": 1},
        {"word": "World", "properties": ["red", "blink", "bggreen"], "spaces": 2},
        {"word": "Bla Bla Bla", "properties": ["green", "underline", "bgred"], "spaces": 3},
    ]

    Console.print(input_data=data_to_print)
