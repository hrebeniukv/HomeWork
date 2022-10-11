# Напишіть декоратор, який перетворює результат роботи функції на стрінг
# Напишіть докстрінг для цього декоратора


def change_to_string(fun):
    """
    This decorator takes a function as an argument and modifies
    to string format the data returned by this function.
    :param fun: decorated function
    :return: wrap function
    """

    def wrap(*args, **kwargs):
        """
        The function can take any quantity of positional and named arguments.
        :param args: positional arguments of decorated function
        :param kwargs: named arguments of decorated function
        :return: the data of decorated function in string format
        """
        return str(fun(*args, **kwargs))

    return wrap
