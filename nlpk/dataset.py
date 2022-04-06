import os.path
from collections import Counter

import pandas as pd


# /home/yatai/PycharmProjects/Machine-Learning-Text-Classifier/data/trg.csv

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
# ^ ?????????????????????????





class Dataset:
    def __init__(self, file_path: str = 'data/trg.csv'):
        """

        :param file_path:
        """
        self.df: pd.Dataframe = pd.read_csv(os.path.join(PROJECT_ROOT, 'data/trg.csv'))
        self.tokenizer = lambda string: string.split(' ')
        pass

    def bow(self):
        counters = []
        for _i, ele in self.df.iterrows():
            ed = ele.to_dict()
            counters.append(Counter(self.tokenizer(ed['abstract'])))
            print()
        pass




if __name__ == "__main__":
    dataset = Dataset()
    dataset.bow()

