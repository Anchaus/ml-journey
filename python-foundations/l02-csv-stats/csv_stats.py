#! /usr/bin/env python3

import argparse
import csv
from numbers import Number
import statistics
from typing import Sequence


def types_parser(types_string: str) -> list:
    types_list = types_string.split(sep=",")
    
    if not all(type in ["num", "text"] for type in types_list):
        raise ValueError("types must be 'num' or 'text'")
    
    return types_list


class CsvStats:
    def __init__(self):
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
            help=("types of csv columns in format 'type1,type2,...'. "
                "Correct types: num, text")
        )
        self.parser = parser
        self._file_name = None

    
    def parse_args(self) -> None:
        args = self.parser.parse_args()
        self._file_name = args.filename
        self._types = args.types
    

    def count_stats(self):
        if self._file_name is None:
            raise self.parser.error(
                message="Arguments must be parsed before count_stats"
            )
            
        with open(file=self._file_name, newline='') as csv_file:
            reader = csv.DictReader(f=csv_file)
            self._field_names = reader.fieldnames

            if self._field_names is None:
                self.parser.error(message=f"File '{self._file_name}' is empty")

            if (self._types is not None
                    and len(self._field_names) != len(self._types)):
                self.parser.error(
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
                for column_num, column_name in enumerate(data.keys()):
                    column = data[column_name]
                    if self._is_column_numeric(column_num, column):
                        column_stats = self._numeric_stats(column)
                    else:
                        column_stats = self._categorical_stats(column)
                    self._stats[column_name] = column_stats
            
            return self._stats

    
    def _is_column_numeric(self, column_num: int, column: list) -> bool:
        if self._types is None:
            return any([isinstance(value, Number) for value in column])
        else:
            return self._types[column_num] == 'num'


    def _numeric_stats(self, column: list) -> dict:
        ...


    def _categorical_stats(self, column: list) -> dict:
        ...


    def get_stats(self) -> dict:
        return self._stats
    

    def get_field_names(self) -> Sequence[str] | None:
        return self._field_names


    def print_stats(self):
        ...


def main() -> None:
    stats = CsvStats()
    stats.parse_args()
    stats.count_stats()
    stats.print_stats()


if __name__ == '__main__':
    main()
