import math
import pandas as pd

from value_investing.strategy_base import StrategyBase
from value_investing.helpers.util import format_currency

class Graham(StrategyBase):
    
    def __init__(self) -> None:
        super().__init__()
        self.strategy_name = "Graham"
    
    def apply_strategy(self, df: pd.DataFrame) -> pd.DataFrame:

        if self.source == "status_invest":
            df['NRO. GRAHAM'] = (df['VPA'] * df['LPA'] * 22.5).apply(lambda x: round(math.sqrt(x), 2))
            df['MARGEM SEGURANCA'] = ((df['NRO. GRAHAM'] - df['PRECO']) / df['PRECO']) * 100
            df.sort_values(by=['MARGEM SEGURANCA'], ascending=False, inplace=True)

            return df

        return None