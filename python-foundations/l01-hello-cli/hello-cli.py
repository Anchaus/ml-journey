#! /usr/bin/python

import argparse


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
        description=(
            "A util that say hello in different "
            "languages by given name"
        ),
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
        nargs='+',
        type=str,
        action='extend',
        choices=HELLO_DICT.keys(),
        help="choice of language to display hello (default: %(default)s)"
    )

    args = parser.parse_args()
    if not args.languages:
        args.languages = ["English"]

    hello_list = [f"{HELLO_DICT[language.capitalize()]}, {args.name}"
                  for language
                  in args.languages]
    print('\n'.join(hello_list))


if __name__ == "__main__":
    main()
