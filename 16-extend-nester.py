import sys


def print_lol(the_list, indent=False, level=0, fh=sys.stdout):
    for line in the_list:
        if isinstance(line, list):
            print_lol(line, indent, level+1, fh)
        else:
            if indent:
                for sta_stop in range(level):
                    print('\t', end='', file=fh)
                print(line, fh)


movies = [
    "The Holy Grail",
    "The Life of Brian",
    "The Meaning of Life",
    [
        "Machael Palin",
        "John CLeeses"
    ]
]

with open('./file/nester_out.txt', 'w') as nester_out:
    print_lol(movies, fh=nester_out)
