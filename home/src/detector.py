from home.src.analyzer import Analyzer
from itertools import combinations
import pandas as pd


class Detector:
    def __init__(self, handler_list, language="english"):
        self.language = language
        self.handler_list = handler_list
        self.analyzer_list = self.setup_pairs()

    def setup_pairs(self):
        analyzer_list = []
        for pair in list(combinations(self.handler_list, 2)):
            analyzer_list.append(Analyzer(pair[0], pair[1], self.language))
        return analyzer_list

    def process(self):
        df_metrics = pd.DataFrame()
        for analyzer in self.analyzer_list:
            df_metrics = df_metrics.append(analyzer.extract_metrics())
        return df_metrics