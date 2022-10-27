import pandas as pd

from value_investing.strategy_base import StrategyBase
from value_investing.helpers.util import format_currency

class Bazin(StrategyBase):
    
    def __init__(self) -> None:
        super().__init__()
        self.strategy_name = "Bazin"
    
    def apply_strategy(self, df: pd.DataFrame) -> pd.DataFrame:

        if self.source == "status_invest":
            col = "DIV. LIQ. / PATRI."
        else:
            col = "DIV.LIQ/ PATRIM."
            df[col] = df[col].apply(lambda x: format_currency(x))

        df[col].fillna(-9999, inplace=True)
        df = df[df[col] <= 1]
        df.sort_values(by=['P/L'], inplace=True)

        return df