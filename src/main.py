# -*- coding: utf-8 -*-
import argparse
import sys
import os

from TextDataReader import TextDataReader
from YamlDataReader import YamlDataReader
from CalcRating import CalcRating
from StudentStatisticsYaml import StudentStatisticsYaml


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def process_txt_file(path):
    reader = TextDataReader()
    students = reader.read(path)
    print("Students: ", students)
    rating = CalcRating(students).calc()
    print("Rating: ", rating)


def process_yaml_file(path):
    reader = YamlDataReader(path)
    reader.read_data()
    students_data = reader.data
    stats = StudentStatisticsYaml(students_data)
    averages = stats.calculate_average_score()
    print("Average scores: ", averages)


def main():
    path = get_path_from_arguments(sys.argv[1:])

    if path.endswith('.txt'):
        process_txt_file(path)
    elif path.endswith('.yaml'):
        process_yaml_file(path)
    else:
        print("Unsupported file format. Use either .txt or .yaml")


if __name__ == "__main__":
    main()
