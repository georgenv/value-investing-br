import pandas as pd

from value_investing.strategy_base import StrategyBase
from value_investing.helpers.util import format_currency

class GreenblattMod(StrategyBase):
    
    def __init__(self) -> None:
        super().__init__()
        self.strategy_name = "Greenblatt_Modificado"
    
    def apply_strategy(self, df: pd.DataFrame) -> pd.DataFrame:

        sort_cols = ["P/L", "ROE"]

        for col in sort_cols:
            df[col] = df[col].apply(lambda x: format_currency(x))

            if col == sort_cols[0]:
                df.sort_values(by=[col], inplace=True)
            else:
                df.sort_values(by=[col], inplace=True, ascending=False)
            
            df[f'RANKING {col}'] = list(range(1, len(df.index) + 1))
                
            df['RANKING FINAL'] += df[f'RANKING {col}']

        df.sort_values(by=['RANKING FINAL'], inplace=True)

        return df
