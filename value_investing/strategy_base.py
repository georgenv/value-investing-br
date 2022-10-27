import pandas as pd
import os

from abc import ABC, abstractmethod
from datetime import date

from value_investing.helpers.util import format_currency, strip_accents


class StrategyBase(ABC):

    def __init__(self) -> None:
        self.source = None
        self.strategy_name = None
        self.ouput_dir = "result"
        os.makedirs(self.ouput_dir, exist_ok=True)
    
    @abstractmethod
    def apply_strategy(self, df: pd.DataFrame) -> pd.DataFrame:
        pass
    
    def read_file(self) -> dict:
        return {
            "csv": lambda fp: pd.read_csv(fp, sep=";", decimal=","),
            "xlsx": lambda fp: pd.read_excel(fp, engine="openpyxl")
        }
    
    def clean_invalid_values(self, df: pd.DataFrame) -> pd.DataFrame:
        df['RANKING FINAL'] = 0
        select_cols = ['P/L', 'P/VP']

        for col in select_cols:
            df[col] = df[col].apply(lambda x: format_currency(x))
            df = df[df[col] > 0]
        
        return df
    
    def export_result(self, df: pd.DataFrame) -> None:
        if (df['RANKING FINAL'] == 0).all():
            df['RANKING FINAL'] = list(range(1, len(df.index) + 1))
            
        filename = f"{self.strategy_name}_{date.today()}.xlsx"
        df.to_excel(f"{self.ouput_dir}{os.path.sep}{filename}", index=False)

    def run(self, file_path: str, source: str) -> None:
        self.source = source
        
        file_type = file_path.split(".")[-1].lower()
        df = self.read_file()[file_type](fp=file_path)

        df.rename(columns=lambda x: strip_accents(x).strip().upper(), inplace=True)
        df = self.clean_invalid_values(df)
        df = self.apply_strategy(df)

        if not df is None:
            self.export_result(df)