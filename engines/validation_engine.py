"""
RT-DOS Intelligence Platform
Module      : Validation Engine
Version     : 1.0.1
Status      : Production
"""


class ValidationEngine:

    REQUIRED_COLUMNS = (
        "Open",
        "High",
        "Low",
        "Close",
        "Volume",
    )

    def __init__(self, minimum_history=50):

        self.minimum_history = minimum_history

    def validate(self, market_data):

        valid_assets = []
        invalid_assets = []

        for asset in market_data:

            valid, reason = self._validate_asset(asset)

            if valid:
                valid_assets.append(asset)
            else:
                invalid_assets.append(
                    {
                        "symbol": asset.get("symbol", "UNKNOWN"),
                        "reason": reason,
                    }
                )

        report = {
            "requested_assets": len(market_data),
            "validated_assets": len(valid_assets),
            "invalid_assets": len(invalid_assets),
            "success": len(invalid_assets) == 0,
            "details": invalid_assets,
        }

        return {
            "valid_assets": valid_assets,
            "invalid_assets": invalid_assets,
            "report": report,
        }

    def _validate_asset(self, asset):

        if asset is None:
            return False, "Asset is None"

        if "symbol" not in asset:
            return False, "Missing symbol"

        history = asset.get("history")

        if history is None:
            return False, "History unavailable"

        if len(history) < self.minimum_history:
            return False, f"Insufficient history ({len(history)} candles)"

        for column in self.REQUIRED_COLUMNS:

            if column not in history.columns:
                return False, f"Missing column: {column}"

        return True, ""
