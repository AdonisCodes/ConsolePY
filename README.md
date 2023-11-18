# ConsolePY

A simple Python script that allows you to print text with different properties to the console.

## Usage

```python
from ConsolePY.console import Console, Property

# Example 1
data_to_print = [
    {"word": "Hello", "properties": ["bold", "underline", "bgblue"], "spaces": 1},
    {"word": "World", "properties": ["red", "blink", "bggreen"], "spaces": 2},
    {"word": "Bla Bla Bla", "properties": ["green", "underline", "bgred"], "spaces": 3},
]

Console.print(input_data=data_to_print)
```

This will print the specified words to the console with the specified properties and spaces in between.

## Properties

The available properties are defined in the `Property` enum. You can use these properties to apply different effects to your text.

Some examples of properties include:

- `Property.BOLD`: Makes the text bold.
- `Property.UNDERLINE`: Underlines the text.
- `Property.ITALIC`: Makes the text italic.
- `Property.BLINK`: Makes the text blink.
- `Property.INVERT`: Inverts the colors of the text.

You can also use properties to change the color of the text and the background color. For example:

- `Property.RED`: Sets the text color to red.
- `Property.BG_GREEN`: Sets the background color to green.

You can combine multiple properties by passing a list of properties to the `properties` parameter.

## Contributions

Contributions are welcome! If you have any suggestions or improvements, feel free to create a pull request.
