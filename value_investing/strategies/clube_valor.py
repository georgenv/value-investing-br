import pandas as pd

from value_investing.strategy_base import StrategyBase
from value_investing.helpers.util import format_currency

class ClubeValor(StrategyBase):
    
    def __init__(self) -> None:
        super().__init__()
        self.strategy_name = "Clube_do_Valor"
    
    def apply_strategy(self, df: pd.DataFrame) -> pd.DataFrame:

        df['ROE'] = df['ROE'].apply(lambda x: format_currency(x))
        df['EV/EBIT'] = df['EV/EBIT'].apply(lambda x: format_currency(x))
        df = df[df['EV/EBIT'] > 0]

        df.sort_values(by=['ROE'], ascending=False, inplace=True)
        df['RANKING ROE'] = list(range(1, len(df.index) + 1))

        df['EARNING YIELD'] = (1 / df['EV/EBIT']) * 100
        df.sort_values(by=['EARNING YIELD'], ascending=False, inplace=True)
        df['RANKING E.Y.'] = list(range(1, len(df.index) + 1))

        df['RANKING FINAL'] = df['RANKING E.Y.'] + df['RANKING ROE']
        df.sort_values(by=['RANKING FINAL'], inplace=True)

        return df
