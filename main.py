import argparse

from value_investing.strategies.strategy_factory import StrategyFactory

# FILTROS
# PL >= 0.1 e <= 13
# P/VP >= 0.1
# LIQ. DIÁRIA >= 871k

def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--file", type=str, required=True,
                        help="Csv file path.")
    parser.add_argument("-s", "--source", type=str, required=True,
                        default="status_invest",
                        choices=["status_invest", "fundamentus"],
                        help="File's source")

    args = parser.parse_args()

    if args.file:
        sf = StrategyFactory()
        strategies = [sf.create_strategy(strategy_name=name) for name in sf.strategies]

        for strategy in strategies:
            strategy.run(file_path=args.file, source=args.source)

if __name__ == "__main__":
    main()