#! /usr/bin/python

import argparse
import sys


def main():
    HELLO_DICT = {
        'English': 'Hello',
        'German': 'Hallo',
        'Spanish': 'Hola',
        'Indonesian': 'Hai',
        'Swedish': 'Hei',
        'Portuguese': 'Bom dia',
        'Chinese': 'Ni hao',
        'Italian': 'Ciao',
        'Hungarian': 'Szia',
        'Polish': 'Cest',
        'Turkish': 'Merehaba'
    }

    parser = argparse.ArgumentParser(
        prog='hello-cli',
        usage='%(prog)s NAME [-l]...',
        description="A util that say hello in different languages by given name",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        'name',
        type=str,
        help="name of person whom to say hello"
    )
    parser.add_argument(
        '-l',
        '--languages',
        type=str,
        action='extend',
        default="English",
        help="choice of language to display hello (default: %(default)s)"
    )
    # TODO list of avaliable languages

    args = parser.parse_args(sys.argv)

    # TODO: error for missing languages

    hello_list = [f"{HELLO_DICT[language.capitalize()]}, {args.name}"
                  for language
                  in args.languages]
    print('\n'.join(hello_list))

if __name__ == "__main__":
    main()
