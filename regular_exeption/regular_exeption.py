import re


# 1. there is a string " name=Amanda=sssss&age=32&&salary=1500&currency=euro ".
# Convert this string to a dictionary {name: Amanda, age: 32, salary: 1500, currency: quro}

test_string = "name=Amanda=sssss&age=32&&salary=1500&currency=euro"


def string_to_dict(my_string):
    pattern = re.compile(r"(\w+)=(\w+)")
    res = pattern.findall(my_string)
    return {i[0]: i[1] for i in res}


print(string_to_dict(test_string))

# 2. you have a list of variable names in camel case format ["FirstItem", "FriendsList", "MyTuple"]
# convert it to a list of variable names for python in snake case format ["first_item", "friends_list", "my_tuple"]

test_list = ["FirstItem", "FriendsList", "MyTuple"]


def camel_to_snake_case(snake_list):
    new_list = []
    pattern = re.compile(r"[A-Z][a-z]*")
    for i in snake_list:
        res = list(map(lambda a: a.lower(), pattern.findall(i)))
        new_list.append(f"{res[0]}_{res[1]}")
    return new_list


print(camel_to_snake_case(test_list))

# 3.you have a text break the text(attached file) into sentences. As a result, you should get a list of sentences.

def parsing_text(file_path):
    with open(file_path, 'r') as my_file:
        text = my_file.read()

    pattern = re.compile(r".*?(?:\s[A-z]+\.+\s|\s[a-z]+\.+)|.+")
    return pattern.findall(text)


print(parsing_text("text"))

# 4. you have html page markup, convert it to structure
# [('google', 'www.google.com', 'Google'), ('facebook', 'http://facebook.com/dign-in', ' Facebook'),
#  ('amazon', 'amazon.com', 'Amazon')]
# using only regular expressions. The first element of the tuple is the id of the container the link is in,
# the second is the link, and the third is the text of the link

def parsing_html(file_path):
    with open(file_path, 'r') as my_file:
        html_doc = my_file.read()
        pattern = re.compile(r"(\b[a-z]{5,}\b).+\s+<a.+?\"(.+)\".+\s+(\b[A-z]+\b)")
    return pattern.findall(html_doc)


print(parsing_html("index.html"))


# 5.* you have the same page markup file, but you need to give out a structure in which not the whole link but only
# the domain name:
# [('google', 'google.com', 'Google'), ('facebook', 'facebook. com', 'Facebook'), ('amazon', 'amazon.com', 'Amazon')]

def parsing_html(file_path):
    with open(file_path, 'r') as my_file:
        html_doc = my_file.read()
        pattern = re.compile(r"(\b[a-z]{5,}\b).+\s+<a.+?([a-z]{4,}\..+[a-z]).+\s+(\b[A-z]+\b)")
    return pattern.findall(html_doc)


print(parsing_html("index.html"))