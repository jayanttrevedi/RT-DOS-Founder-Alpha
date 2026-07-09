"""
RT-DOS Intelligence Platform
Module      : Consistency Engine
Version     : 1.0.0
Status      : Production
Architecture: Core Intelligence Layer

Purpose
-------
Ensures every analysis engine returns the same set of symbols
before Composite Engine executes.
"""


class ConsistencyEngine:

    def validate(
        self,
        technical,
        momentum,
        atr,
        volume,
        relative_strength,
    ):

        datasets = {
            "Technical": technical,
            "Momentum": momentum,
            "ATR": atr,
            "Volume": volume,
            "Relative Strength": relative_strength,
        }

        symbol_sets = {
            name: {item["symbol"] for item in data} for name, data in datasets.items()
        }

        reference_name = next(iter(symbol_sets))
        reference = symbol_sets[reference_name]

        inconsistencies = []

        for name, symbols in symbol_sets.items():

            missing = sorted(reference - symbols)
            extra = sorted(symbols - reference)

            if missing or extra:

                inconsistencies.append(
                    {
                        "engine": name,
                        "missing": missing,
                        "extra": extra,
                    }
                )

        report = {
            "success": len(inconsistencies) == 0,
            "reference_engine": reference_name,
            "asset_count": len(reference),
            "details": inconsistencies,
        }

        return report
