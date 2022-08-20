import tkinter
import time
import datetime as datetime
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt


wallet_address = "0x81ab16780331760e7f0501049ba86ed93c69e997"
etherscan_api_key = "I3WYRGV1MAZ1RD541S58JU4413USYVABEK"
eth = 10**18


ether_url = "https://api.etherscan.io/api"


def api_url(module, action, address, **kwargs):
    url = (
        ether_url
        + f"?module={module}&action={action}&address={address}&apikey={etherscan_api_key}"
    )

    for key, value in kwargs.items():
        url += f"&{key}={value}"
    return url


# print(get_balance_url)
def get_balance(address):
    get_balance_url = api_url("account", "balance", wallet_address, tag="latest")
    results = requests.get(get_balance_url)
    etherscan_result = results.json()
    balance = int(etherscan_result["result"]) / eth
    return balance


def get_transcations(address):
    get_transcations_url = api_url(
        "account",
        "txlist",
        address,
        startblock=0,
        endblock=99999999,
        page=1,
        offset=10000,
        sort="asc",
    )
    results = requests.get(get_transcations_url)
    etherscan_result = results.json()["result"]

    current_balance = 0
    balances = []
    times = []

    internal_url = api_url(
        "account",
        "txlistinternal",
        address,
        startblock=0,
        endblock=99999999,
        page=1,
        offset=10000,
        sort="asc",
    )
    response2 = requests.get(internal_url)
    etherscan_result2 = response2.json()["result"]
    etherscan_result.extend(etherscan_result2)
    etherscan_result.sort(key=lambda x: int(x["timeStamp"]))

    for tx in etherscan_result:
        to = tx["to"]
        from_ = tx["from"]
        value = int(tx["value"]) / eth
        if "gasPrice" in tx:
            gas = int(tx["gasUsed"]) * int(tx["gasPrice"]) / eth
        else:
            gas = int(tx["gasUsed"]) / eth
        timestamp = datetime.datetime.fromtimestamp(int(tx["timeStamp"]))
        money_in = to.lower() == wallet_address.lower()

        if money_in:
            current_balance += value
        else:
            current_balance -= value + gas

        balances.append(current_balance)
        times.append(timestamp)
    plt.plot(times, balances)
    plt.show()


get_transcations(wallet_address)
