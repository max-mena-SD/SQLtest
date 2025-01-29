import json
import pandas as pd


class JsonManipulation:
    def __init__(self, json_location):
        self.json_location = json_location

    def load_file(self) -> pd.DataFrame:

        with open("datasnap.json", "r") as file:
            datasnap = json.load(file)
        df_datasnap = pd.DataFrame(datasnap)

        return df_datasnap
