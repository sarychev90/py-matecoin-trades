from decimal import Decimal
import json


def calculate_profit(filename: str) -> None:
    tardes = {}
    profits = {"earned_money": "0", "matecoin_account": "0"}
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    with open(filename, "r") as file:
       tardes = json.load(file)
    for tarde in tardes:
        if tarde["bought"]:
            earned_money -= Decimal(tarde["matecoin_price"]) * Decimal(tarde["bought"])
            matecoin_account += Decimal(tarde["bought"])
        if tarde["sold"]:
            earned_money += Decimal(tarde["matecoin_price"]) * Decimal(tarde["sold"])
            matecoin_account -= Decimal(tarde["sold"])
    profits["earned_money"] = str(earned_money)
    profits["matecoin_account"] = str(matecoin_account)

    with open("profit.json", "w") as file:
        json.dump(profits, file, indent=2)
