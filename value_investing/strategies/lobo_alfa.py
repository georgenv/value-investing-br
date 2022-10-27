"""
Lucro constante (3 anos) e ordernar por PL
"""

import pandas as pd

from value_investing.strategy_base import StrategyBase

class LoboAlfa(StrategyBase):
    
    def __init__(self) -> None:
        super().__init__()
        self.strategy_name = "Lobo_Alfa"
    
    def apply_strategy(self, df: pd.DataFrame) -> pd.DataFrame:
        
        df.sort_values(by=['P/L'], inplace=True)
        return df