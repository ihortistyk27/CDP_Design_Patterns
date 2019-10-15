
def decorate_my_function(original_function):
    """Decorates a function by wrapping its return value in a pair of HTML paragraph tags."""

    def add_additional_text():
        # Obtain string returned by original function
        text_from_original_function = original_function()
        # Adding new functionality to the function being decorated
        return "<p>" + text_from_original_function + "</p>"

    return add_additional_text()


@decorate_my_function
def function_to_be_decorated():
    """A simple function that returns a string."""
    return " Example of Decorator Pattern, #CDP#."


print(function_to_be_decorated)
