import ast
import collections
import matplotlib.pyplot as plt
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


def create_activity_graph(data_dicts):
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax.set_title('Fatzilla')
    ax.set_xlabel('Date')
    ax.set_ylabel('# Activities')
    
    activity_dates = os.listdir('dicts')
    
    activity_counters = []
    for data_dict in data_dicts:
        activity_counters.append(len(data_dict))
    
    ax.bar(activity_dates, activity_counters, width=0.1)
    
    plt.xticks(range(0, max(activity_counters), 1))
    plt.savefig('fatzilla.png')
    plt.show()
    

def main():
    data_dicts = collect_data()
    
    print(accumulate_data(data_dicts))
    create_activity_graph(data_dicts)
    

if __name__ == '__main__':
    main()
