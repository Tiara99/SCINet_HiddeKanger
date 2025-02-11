import pandas as pd

def load_data(data_name, pairs):

    df = pd.read_csv('/content/SCINet_lab_A/exp/reprod/data/Data_preprocessed/' + data_name + '.csv').dropna()

    mean = df.mean()
    std = df.std()

    df = df.swapaxes("index", "columns")

    data = {}

    for idx, pair in enumerate(pairs):
        data[pair] = df.iloc[idx]

    return data, mean, std
