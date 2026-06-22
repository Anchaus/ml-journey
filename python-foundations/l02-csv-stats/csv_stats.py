#! /usr/bin/env python3

import argparse
import csv
from numbers import Number
import statistics


class CsvStats:
    def __init__(self, file_name: str, types: list):
        self._file_name = file_name
        self.types = types
    

    def count_stats(self):
        with open(self.file_name, newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            self._field_names = reader.fieldnamess

            if (self._types is not None
                    and len(self._field_names) != len(self._types)):
                raise argparse.ArgumentError(
                    message="Types must be same length as number of columns"
                )
        
            # Extract data in dict
            data = {column_name: [] for column_name in self._field_names}
            for row in reader:
                for column_name in self._field_names:
                    try:
                        data[column_name].append(float(row[column_name]))
                    except (ValueError, TypeError):
                        data[column_name].append(row[column_name])

            self._stats = {column_name: {}
                           for column_name
                           in self._field_names}

            # Calc stats
            if self._types is None:
                for column_name in data.keys():
                    column = data[column_name]
                    if any(isinstance(column, Number)):
                        column_stats = self._numeric_stats(column)
                    else:
                        column_stats = self._categorical_stats(column)
                    self._stats[column_name] = column_stats
            else:
                for column_name, type in zip(data.keys(), self._types):
                    column = data[column_name]
                    if type == 'num':
                        column_stats = self._numeric_stats(column)
                    else:
                        column_stats = self._categorical_stats(column)
                    self._stats[column_name] = column_stats
            
            return self._stats


    def _numeric_stats(self, column: list) -> dict:
        ...


    def _categorical_stats(self, column: list) -> dict:
        ...


    def get_stats(self) -> dict:
        return self._stats
    

    def get_field_names(self) -> list:
        return self._field_names


    def print_stats(self):
        ...


def types_parser(types_string: str) -> list:
    try:
        types_list = types_string.split(",")
    except AttributeError:
        raise argparse.ArgumentError(
            message="types must be in format  'type1,type2,...'"
        )
    
    if not all(type in ["num", "text"] for type in types_list):
        raise argparse.ArgumentError(message="types must be 'num' or 'text'")
    
    return types_list


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="csv_stats",
        usage="csv_stats FILE_NAME [-t type1,type2,...]",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "file_name",
        type=str
    )
    parser.add_argument(
        "-t", "--types",
        type=types_parser,
        help=("types of csv columns in format 'type1,type2,...'. ",
              "Correct types: num, text")
    )
    args = parser.parse_args()

    stats = CsvStats(args.file_name, args.types)
    stats.count_stats()
    stats.print_stats()


if __name__ == '__main__':
    main()
