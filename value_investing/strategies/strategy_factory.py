from value_investing.strategy_base import StrategyBase
from value_investing.strategies.greenblatt import Greenblatt
from value_investing.strategies.graham import Graham
from value_investing.strategies.bazin import Bazin
from value_investing.strategies.clube_valor import ClubeValor
from value_investing.strategies.low_value import LowValue
from value_investing.strategies.lobo_alfa import LoboAlfa
from value_investing.strategies.greenblatt_mod import GreenblattMod


class SingletonMeta(type):
    """
    The design pattern Singleton implemented as metaclass, it ensures that will be only
    one instance of StocksRetriever class.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class StrategyFactory(metaclass=SingletonMeta):

    def __init__(self) -> None:

        self.strategies = {
            "greenblatt": Greenblatt(),
            "greenblatt_mod": GreenblattMod(),
            "bazin": Bazin(),
            "graham": Graham(),
            "clube_valor": ClubeValor(),
            "low_value": LowValue(),
            "lobo_alfa": LoboAlfa(),
        }
    
    def create_strategy(self, strategy_name: str) -> StrategyBase:
        return self.strategies[strategy_name]