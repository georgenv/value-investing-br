import pandas as pd

from value_investing.strategy_base import StrategyBase
from value_investing.helpers.util import format_currency

class LowValue(StrategyBase):
    
    def __init__(self) -> None:
        super().__init__()
        self.strategy_name = "Descontadas"
    
    def apply_strategy(self, df: pd.DataFrame) -> pd.DataFrame:
        
        df.sort_values(by=['P/VP'], inplace=True)
        df['RANKING P/VP'] = list(range(1, len(df.index) + 1))

        df.sort_values(by=['P/L'], inplace=True)
        df['RANKING P/L'] = list(range(1, len(df.index) + 1))

        df['RANKING FINAL'] = df['RANKING P/VP'] + df['RANKING P/L']
        df.sort_values(by=['RANKING FINAL'], inplace=True)

        df['ROE'] = df['ROE'].apply(lambda x: format_currency(x))

        return df