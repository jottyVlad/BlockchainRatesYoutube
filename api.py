from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP

import requests

@dataclass
class BlockchainRatesInfo:
    symbol: str
    price: Decimal

    def __str__(self):
        return f"За 1 {self.symbol} дают {self.price} USD"


class BlockchainRates:
    @property
    def url(self):
        return "https://api.coincap.io/v2/assets"

    @property
    def header(self):
        return "Курс криптовалюты: \n\n"

    def get(self, symbol):
        result = (requests.get(self.url).json())["data"]
        message = ""
        for currency in result:
            if currency["symbol"] == symbol:
                message = self.header
                price = Decimal(currency["priceUsd"])
                price = price.quantize(Decimal("1.0000"), ROUND_HALF_UP)
                message += str(BlockchainRatesInfo(
                    symbol=currency["symbol"],
                    price=price
                ))

        return message