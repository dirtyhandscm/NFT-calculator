import tkinter
import datetime


# nft profit calculator
def profit_calculator():
    ppg = float(ppg_entry.get())

    roi_percentage = float(roi.get())
    royalty_percentage = float(royalty.get())
    needed_price = ppg * roi_percentage
    profits = needed_price - ppg
    print(needed_price)
    price_plus_royalty = round(
        needed_price + (needed_price * (royalty_percentage / 100)), 2
    )
    print(price_plus_royalty)
    answer.config(text=price_plus_royalty, font=("Arial", 20))

    print("Price plus royalty: " + str(price_plus_royalty))
    print("Profit: " + str(profits))
    return price_plus_royalty, profits


# write to a text file with the current date and time and the profit calculator output and rio_percentage
def log_sale():
    with open("profit_calculator_log.txt", "a") as f:
        f.write(
            str(datetime.datetime.now())
            + ": "
            + str(profit_calculator())
            + " Sale "
            + str(ppg_entry.get())
            + " Price paid \n"
            + str(roi.get())
            + " ROI "
            + str(royalty.get())
            + " Royalty \n"
            + str()
        )


window = tkinter.Tk()
window.title("NFT Profit Calculator")
window.minsize(width=300, height=300)


# calculated price
answer = tkinter.Label(
    window,
)
answer.grid(row=5, column=1)


# label for input
input_label = tkinter.Label(window, text="Price paid + Gas:")
input_label.grid(row=0, column=0)

# input for price paid
ppg_entry = tkinter.Entry(window)
ppg_entry.focus_force()
ppg_entry.grid(row=0, column=1)

# lesson_learned = tkinter.Text(height=10, width=35)
# lesson_learned.insert(tkinter.END, "Lesson Learned from this trade:")
# print
# lesson_learned.grid(row=8, column=0)


# label for input
roi_label = tkinter.Label(window, text="ROI% (ex. 2 = 200%):")
roi_label.grid(row=2, column=0)

# input for price paid
roi = tkinter.Entry(window)
roi.grid(row=2, column=1)


# label for input
royalty_label = tkinter.Label(window, text="Royalty % 1 = 1% :")
royalty_label.grid(row=3, column=0)

# input for price paid
royalty = tkinter.Entry(window)
royalty.insert(0, "0")
royalty.grid(row=3, column=1)

button = tkinter.Button(
    window,
    text="Calculate",
    command=profit_calculator,
)
button.grid(row=4, column=1)

log_profits = tkinter.Button(window, text="Log profits", command=log_sale)
log_profits.grid(row=6, column=1)

window.mainloop()
