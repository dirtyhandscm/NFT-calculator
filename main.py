# nft profit calculator
import tkinter


def profit_calculator():
    ppg = float(input.get())
    royalty_percentage = float(input.get())
    roi_percentage = float(input.get())
    needed_price = ppg * roi_percentage
    price_plus_royalty = needed_price + (needed_price * royalty_percentage)
    print("Price plus royalty: " + str(price_plus_royalty))


profit_calculator()
