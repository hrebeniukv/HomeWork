import sys

from WorkWithfile.letter_counter import Counter


def custom_print(*args, custom_sep=" ", custom_end=None):
    """
    :param args: argument that will print
    :param custom_sep: separator, which will add between elements, if there are more one element for print,
        by default the separator is set as " " (spacing)
    :param custom_end: element which will add on the end of print, by default is set as None
    :return:
    """
    print_data = ""
    qty_arg = len(args)

    for i in range(qty_arg):
        element = str(args[i])
        if i < qty_arg - 1:
            print_data += element
            print_data += str(custom_sep)
        else:
            print_data += element

    if custom_end:
        print_data += str(custom_end)

    sys.stdout.write(print_data)


count_letter = Counter("text.txt")
for key, value in count_letter.get_counted_letter.items():
    custom_print(f"{key}: {value}", custom_end="\n")
