import ast
import collections
import os

def collect_data():
    data_dicts = []
    raw_files = os.listdir('dicts')
    for raw_file in raw_files:
        with open('dicts/' + raw_file) as fd:
            raw_data = fd.read()
            py_dict = ast.literal_eval(raw_data)
            data_dicts.append(py_dict)
    return data_dicts


def accumulate_data(data_dicts):
    c = collections.Counter()
    for data_dict in data_dicts:
        c.update(data_dict)
    return c


def main():
    print(accumulate_data(collect_data()))
    

if __name__ == '__main__':
    main()
