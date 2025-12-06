
#Imports
from bakery import assert_equal
import matplotlib.pyplot as plt
from drafter import *
from dataclasses import dataclass
import random


#Dataclasses
@dataclass
class Share:
    purchase_price: float
    num_shares: float


@dataclass
class Stock:
    symbol: str
    name: str
    description: str
    price: float
    shares: list[Share]
    stock_history: list[float]


@dataclass
class State:
    username: str
    portfolio: list[Stock]
    portfolio_history: list[float]
    cash: float
    event_status: str


#CONSTANTS


STARTING_WALLET = 1000.0


#Stocks
# 1. Technology / AI (High Price, High Volatility)
tech_stock = Stock(
    symbol="NEURO",
    name="NeuroLink Systems",
    description="A cutting-edge tech firm specializing in neural interface chips.",
    price=245.50,
    shares=[],  # Currently no shares owned
    stock_history=[230.10, 235.00, 240.50, 238.20, 245.50]
)


# 2. Renewable Energy (Medium Price, Steady Growth)
energy_stock = Stock(
    symbol="SOLA",
    name="Solaris Dynamics",
    description="Global leader in renewable energy infrastructure and solar panels.",
    price=45.75,
    shares=[],
    stock_history=[42.00, 42.50, 43.10, 44.00, 45.75]
)


# 3. Consumer Goods / Food (Low Price, Stable)
food_stock = Stock(
    symbol="CRUNCH",
    name="Crunchy Corp",
    description="International snack food conglomerate known for spicy chips.",
    price=12.30,
    shares=[],
    stock_history=[12.10, 12.15, 12.20, 12.25, 12.30]
)


# 4. Defense
defense_stock = Stock(
    symbol="ADCX",
    name="Aegis Dynamics Corporation",
    description="A next-generation defense systems firm specializing in autonomous drone swarms and AI-enhanced battlefield intelligence.",
    price=149.20,
    shares=[],
    stock_history=[142.30, 145.10, 147.85, 150.60, 149.20]
)


# 5. Automotive
automotive_stock = Stock(
    symbol="VLTM",
    name="Voltara Motors",
    description="An electric-vehicle manufacturer known for ultralight battery architecture and high-efficiency autonomous driving systems.",
    price=66.20,
    shares=[],
    stock_history=[62.40, 63.75, 65.10, 64.55, 66.20]
)


STOCKS = [tech_stock, energy_stock, food_stock, defense_stock, automotive_stock]


#Images
trading_floor_image = "trading_floor.png"
failed_transaction_image = "failed_transaction.png"
successful_transaction_image = "successful_transaction.png"
successful_sell_order_image = "successful_sell_order.png"
nuerolink_image = "neurolink.png"
solaris_image = "solaris.png"
crunchy_image = "crunchy.png"
aegis_image = "aegis.png"
voltara_image = "voltara.png"
home_image = "home.png"


#Helper Functions
def calculate_portfolio_value(portfolio: list[Stock]) -> float:
    total = 0.0
    for stock in portfolio:
        for share in stock.shares:
            total += stock.price * share.num_shares
    return total




#Routes
set_website_style("tacit")


@route
def index(state: State) -> Page:
    if not state.portfolio:
        return Page(state, [
            Header("Welcome to Stonks: The Stock Market Game!"),
            Button("Trade", trading_floor),
            Button("New Day", new_day),
            Button("Event", event)
        ])
    else:
        plt.plot(state.portfolio_history)
        plt.xlabel("Days")
        plt.ylabel("Portfolio Value")
        plt.title("Portfolio Value Over Time")
        return Page(state,
        [
            Header("Welcome to Stonks: The Stock Market Game!"),
            Image(home_image, 768, 432),
            f"Cash Available: ${state.cash}",
            f"Portfolo Value: ${calculate_portfolio_value(state.portfolio)}",
            state.event_status,
            MatPlotLibPlot(),
            Button("Trade", "trading_floor"),
            Button("New Day", new_day),
            Button("Event", event),
        ])




@route
def trading_floor(state: State) -> Page:
    return Page(state,[
        Header("Trading Floor"),
        Image(trading_floor_image, 768, 432),
        Button("NeuroLink Systems", view_neuro),
        Button("Solaris Dynamics", view_sola),
        Button("Crunchy Corp", view_crunch),
        Button("VAegis Defense Corporation", view_agcx),
        Button("Voltara Motors", view_vltm),
        Button("Back to Main", index)
    ])


@route
def view_neuro(state: State) -> Page:
    plt.plot(state.portfolio[0].stock_history)
    plt.xlabel("Days")
    plt.ylabel("Stock Price")
    plt.title("NeuroLink Systems (NEURO) Stock Price Over Time")
    Buttons = []
    for i ,share in enumerate(state.portfolio[0].shares):
        Buttons.append(Button("Share Quantity: " + str(share.num_shares) + " | Purchase Price: $" + str(share.purchase_price), sell, [Argument("stock_id", 0), Argument("share_index", i)]))
    return Page(state,[
        Header("NeuroLink Systems (NEURO)"),
        Image(nuerolink_image, 768, 432),
        state.portfolio[0].description,
        "Current Price: $" + str(state.portfolio[0].price),
        MatPlotLibPlot(),
        TextBox("share_quantity", "Number of Shares to Buy"),
        Button("Buy", buy, [Argument("stock_id", 0)]),
        "Below are your owned shares of NeuroLink Systems (NEURO):",
        "Click the share to sell it.",
        BulletedList(Buttons),
        Button("Trade", trading_floor),
        Button("Home", index)
    ])


@route
def view_sola(state: State) -> Page:
    plt.plot(state.portfolio[1].stock_history)
    plt.xlabel("Days")
    plt.ylabel("Stock Price")
    plt.title("Solaris Dynamics (SOLA) Stock Price Over Time")
    Buttons = []
    for i ,share in enumerate(state.portfolio[1].shares):
        Buttons.append(Button("Share Quantity: " + str(share.num_shares) + " | Purchase Price: $" + str(share.purchase_price), sell, [Argument("stock_id", 1), Argument("share_index", i)]))
    return Page(state,[
        Header("Solaris Dynamics (SOLA)"),
        Image(solaris_image, 768, 432),
        state.portfolio[1].description,
        "Current Price: $" + str(state.portfolio[1].price),
        MatPlotLibPlot(),
        TextBox("share_quantity", "Number of Shares to Buy"),
        Button("Buy", buy, [Argument("stock_id", 1)]),
        "Below are your owned shares of Solaris Dynamics (SOLA):",
        "Click the share to sell it.",
        BulletedList(Buttons),
        Button("Trade", trading_floor),
        Button("Home", index)
    ])


@route
def view_crunch(state: State) -> Page:
    plt.plot(state.portfolio[2].stock_history)
    plt.xlabel("Days")
    plt.ylabel("Stock Price")
    plt.title("Crunchy Corp (CRUNCH) Stock Price Over Time")
    Buttons = []
    for i ,share in enumerate(state.portfolio[2].shares):
        Buttons.append(Button("Share Quantity: " + str(share.num_shares) + " | Purchase Price: $" + str(share.purchase_price), sell, [Argument("stock_id", 2), Argument("share_index", i)]))
    return Page(state,[
        Header("Crunchy Corp (CRUNCH)"),
        Image(crunchy_image, 768, 432),
        state.portfolio[2].description,
        "Current Price: $" + str(state.portfolio[2].price),
        MatPlotLibPlot(),
        TextBox("share_quantity", "Number of Shares to Buy"),
        Button("Buy", buy, [Argument("stock_id", 2)]),
        "Below are your owned shares of Crunchy Corp (CRUNCH):",
        "Click the share to sell it.",
        BulletedList(Buttons),
        Button("Trade", trading_floor),
        Button("Home", index)
    ])


@route
def view_agcx(state: State) -> Page:
    plt.plot(state.portfolio[3].stock_history)
    plt.xlabel("Days")
    plt.ylabel("Stock Price")
    plt.title("Aegis Defense Corporation (AGCX) Stock Price Over Time")
    Buttons = []
    for i ,share in enumerate(state.portfolio[3].shares):
        Buttons.append(Button("Share Quantity: " + str(share.num_shares) + " | Purchase Price: $" + str(share.purchase_price), sell, [Argument("stock_id", 3), Argument("share_index", i)]))
    return Page(state,[
        Header("Aegis Defense Corporation (AGCX)"),
        Image(Aegis_image, 768, 432),
        state.portfolio[3].description,
        "Current Price: $" + str(state.portfolio[3].price),
        MatPlotLibPlot(),
        TextBox("share_quantity", "Number of Shares to Buy"),
        Button("Buy", buy, [Argument("stock_id", 3)]),
        "Below are your owned shares of Aegis Defense Corporation (AGCX):",
        "Click the share to sell it.",
        BulletedList(Buttons),
        Button("Trade", trading_floor),
        Button("Home", index)
    ])


@route
def view_vltm(state: State) -> Page:
    plt.plot(state.portfolio[4].stock_history)
    plt.xlabel("Days")
    plt.ylabel("Stock Price")
    plt.title("Voltara Motors (VLTM) Stock Price Over Time")
    Buttons = []
    for i ,share in enumerate(state.portfolio[4].shares):
        Buttons.append(Button("Share Quantity: " + str(share.num_shares) + " | Purchase Price: $" + str(share.purchase_price), sell, [Argument("stock_id", 4), Argument("share_index", i)]))
    return Page(state,[
        Header("Voltara Motors (VLTM)"),
        Image(voltara_image, 768, 432),
        state.portfolio[4].description,
        "Current Price: $" + str(state.portfolio[4].price),
        MatPlotLibPlot(),
        TextBox("share_quantity", "Number of Shares to Buy"),
        Button("Buy", buy, [Argument("stock_id", 4)]),
        "Below are your owned shares of Voltara Motors (VLTM):",
        "Click the share to sell it.",
        BulletedList(Buttons),
        Button("Trade", trading_floor),
        Button("Home", index)
    ])




@route
def buy(state: State, stock_id: int, share_quantity: float) -> Page:
    if (stock_id == 0):
        if share_quantity*state.portfolio[stock_id].price > state.cash:
            return Page(state, [
                Image(failed_transaction_image, 768, 432),
                "Oops! Invalid transaction! You do not have enough funds to buy " + str(share_quantity) + " of " + state.portfolio[stock_id].name,
                Button("Return to " + state.portfolio[stock_id].symbol, view_neuro),
                Button("Trade", trading_floor),
                Button("Home", index)
            ])
        else:
            state.cash = state.cash - share_quantity*state.portfolio[stock_id].price
            state.portfolio[stock_id].shares.append(Share(state.portfolio[stock_id].price, share_quantity))
            return Page(state, [
                Image(successful_transaction_image, 768, 432),
                "Successful transaction! You successfully bought " + str(share_quantity) + " of " + state.portfolio[stock_id].name,
                Button("Return to " + state.portfolio[stock_id].symbol, view_neuro),
                Button("Trade", trading_floor),
                Button("Home", index)
            ])
    elif (stock_id == 1):
        if share_quantity*state.portfolio[stock_id].price > state.cash:
            return Page(state, [
                Image(failed_transaction_image, 768, 432),
                Header("Oops! Invalid transaction! You do not have enough funds to buy " + str(share_quantity) + " of " + state.portfolio[stock_id].name),
                Button("Return to " + state.portfolio[stock_id].symbol, view_sola),
                Button("Trade", trading_floor),
                Button("Home", index)
            ])
        else:
            state.cash = state.cash - share_quantity*state.portfolio[stock_id].price
            state.portfolio[stock_id].shares.append(Share(state.portfolio[stock_id].price, share_quantity))
            return Page(state, [
                Image(successful_transaction_image, 768, 432),
                Header("Successful transaction! You successfully bought " + str(share_quantity) + " of " + state.portfolio[stock_id].name),
                Button("Return to " + state.portfolio[stock_id].symbol, view_sola),
                Button("Trade", trading_floor),
                Button("Home", index)
            ])
    elif (stock_id == 2):
        if share_quantity*state.portfolio[stock_id].price > state.cash:
            return Page(state, [
                Image(failed_transaction_image, 768, 432),
                Header("Oops! Invalid transaction! You do not have enough funds to buy " + str(share_quantity) + " of " + state.portfolio[stock_id].name),
                Button("Return to " + state.portfolio[stock_id].symbol, view_crunch),
                Button("Trade", trading_floor),
                Button("Home", index)
            ])
        else:
            state.cash -= share_quantity*state.portfolio[stock_id].price
            state.portfolio[stock_id].shares.append(Share(state.portfolio[stock_id].price, share_quantity))
            return Page(state, [
                Image(successful_transaction_image, 768, 432),
                Header("Successful transaction! You successfully bought " + str(share_quantity) + " of " + state.portfolio[stock_id].name),
                Button("Return to " + state.portfolio[stock_id].symbol, view_crunch),
                Button("Trade", trading_floor),
                Button("Home", index)
            ])
    elif (stock_id == 3):
        if share_quantity*state.portfolio[stock_id].price > state.cash:
            return Page(state, [
                Image(failed_transaction_image, 768, 432),
                Header("Oops! Invalid transaction! You do not have enough funds to buy " + str(share_quantity) + " of " + state.portfolio[stock_id].name),
                Button("Return to " + state.portfolio[stock_id].symbol, view_agcx),
                Button("Trade", trading_floor),
                Button("Home", index)
            ])
        else:
            state.cash = state.cash - share_quantity*state.portfolio[stock_id].price
            state.portfolio[stock_id].shares.append(Share(state.portfolio[stock_id].price, share_quantity))
            return Page(state, [
                Image(successful_transaction_image, 768, 432),
                Header("Successful transaction! You successfully bought " + str(share_quantity) + " of " + state.portfolio[stock_id].name),
                Button("Return to " + state.portfolio[stock_id].symbol, view_agcx),
                Button("Trade", trading_floor),
                Button("Home", index)
            ])
    elif (stock_id == 4):
        if share_quantity*state.portfolio[stock_id].price > state.cash:
            return Page(state, [
                Image(failed_transaction_image, 768, 432),  
                Header("Oops! Invalid transaction! You do not have enough funds to buy " + str(share_quantity) + " of " + state.portfolio[stock_id].name),
                Button("Return to " + state.portfolio[stock_id].symbol, view_vltm),
                Button("Trade", trading_floor),
                Button("Home", index)
            ])
        else:
            state.cash = state.cash - share_quantity*state.portfolio[stock_id].price
            state.portfolio[stock_id].shares.append(Share(state.portfolio[stock_id].price, share_quantity))
            return Page(state, [
                Image(successful_transaction_image, 768, 432),
                Header("Successful transaction! You successfully bought " + str(share_quantity) + " of " + state.portfolio[stock_id].name),
                Button("Return to " + state.portfolio[stock_id].symbol, view_vltm),
                Button("Trade", trading_floor),
                Button("Home", index)
            ])
    else:
        print("wrong id")


@route
def sell(state: State, stock_id: int, share_index: int, share_quantity: str) -> Page:
    sold_shares = state.portfolio[stock_id].shares[share_index].num_shares
    if (stock_id == 0):
        state.cash += state.portfolio[stock_id].shares[share_index].num_shares*state.portfolio[stock_id].price
        state.portfolio[stock_id].shares.pop(share_index)
        return Page(state, [
            Image(successful_sell_order_image, 768, 432),
            "Congratulations! You just sold " + str(sold_shares) + " shares of " + state.portfolio[stock_id].name + "! You made ",
            Button("Return to " + state.portfolio[stock_id].symbol, view_neuro),
                Button("Trade", trading_floor),
                Button("Home", index)
        ])
    elif (stock_id == 1):
        state.cash += state.portfolio[stock_id].shares[share_index].num_shares*state.portfolio[stock_id].price
        state.portfolio[stock_id].shares.pop(share_index)
        return Page(state, [
            Image(successful_sell_order_image, 768, 432),
            "Congratulations! You just sold " + str(sold_shares) + " shares of " + state.portfolio[stock_id].name + " at " + str(state.portfolio[stock_id].price) + "You made",
            Button("Return to " + state.portfolio[stock_id].symbol, view_sola),
                Button("Trade", trading_floor),
                Button("Home", index)
        ])
    elif (stock_id == 2):
        state.cash += state.portfolio[stock_id].shares[share_index].num_shares*state.portfolio[stock_id].price
        state.portfolio[stock_id].shares.pop(share_index)
        return Page(state, [
            Image(successful_sell_order_image, 768, 432),
            "Congratulations! You just sold " + str(sold_shares) + " shares of " + state.portfolio[stock_id].name + " at " + str(state.portfolio[stock_id].price) + "You made",
            Button("Return to " + state.portfolio[stock_id].symbol, view_crunch),
                Button("Trade", trading_floor),
                Button("Home", index)
        ])
    elif (stock_id == 3):
        state.cash += state.portfolio[stock_id].shares[share_index].num_shares*state.portfolio[stock_id].price
        state.portfolio[stock_id].shares.pop(share_index)
        return Page(state, [
            Image(successful_sell_order_image, 768, 432),
            "Congratulations! You just sold " + str(sold_shares) + " shares of " + state.portfolio[stock_id].name + " at " + str(state.portfolio[stock_id].price) + "You made",
            Button("Return to " + state.portfolio[stock_id].symbol, view_agcx),
                Button("Trade", trading_floor),
                Button("Home", index)
        ])
    elif (stock_id == 4):
        state.cash += state.portfolio[stock_id].shares[share_index].num_shares*state.portfolio[stock_id].price
        state.portfolio[stock_id].shares.pop(share_index)
        return Page(state, [
            Image(successful_sell_order_image, 768, 432),
            "Congratulations! You just sold " + str(sold_shares) + " shares of " + state.portfolio[stock_id].name + " at " + str(state.portfolio[stock_id].price) + "You made" ,
            Button("Return to " + state.portfolio[stock_id].symbol, view_vltm),
                Button("Trade", trading_floor),
                Button("Home", index)
        ])
    else:
        print("wrong stock_id")
   
@route
def new_day(state: State) -> Page:
    state.portfolio_history.append(calculate_portfolio_value(state.portfolio))
    increment = random.randint(-15, +15) / 100 + 1.0
    state.portfolio[0].price = state.portfolio[0].price * increment
    state.portfolio[0].stock_history.append(state.portfolio[0].price)


    increment = random.randint(-5, +5) / 100 + 1.0
    state.portfolio[1].price = state.portfolio[1].price * increment
    state.portfolio[1].stock_history.append(state.portfolio[1].price)


    increment = random.randint(-5, +5) / 100 + 1.0
    state.portfolio[2].price = state.portfolio[2].price * increment
    state.portfolio[2].stock_history.append(state.portfolio[2].price)


    increment = random.randint(-8, +10) / 100 + 1.0
    state.portfolio[3].price = state.portfolio[3].price * increment
    state.portfolio[3].stock_history.append(state.portfolio[3].price)


    increment = random.randint(-8, +5) / 100 + 1.0
    state.portfolio[4].price = state.portfolio[4].price * increment
    state.portfolio[4].stock_history.append(state.portfolio[4].price)


    return index(state)


@route
def event(state: State) -> Page:
    rand = random.randint(1, 5)
    #pandemic
    if(rand == 1):
        increment = 0.75
        for stock in state.portfolio:
            stock.price = stock.price * increment
        state.portfolio_history.append(calculate_portfolio_value(state.portfolio))
        state.event_status = "Global Health Agencies Race to Contain Rapidly Spreading Aurelia Virus After First International Cases Reported."
           
    #interest rate cuts
    elif(rand == 2):
        increment = 1.1
        for stock in state.portfolio:
            stock.price = stock.price * increment
        state.portfolio_history.append(calculate_portfolio_value(state.portfolio))
        state.event_status = "Federal Reserve Announces Surprise Interest Rate Cuts Amid Signs of Slowing Economic Growth."


    #cyberwar
    elif(rand == 3):
        state.portfolio[0].price*1.3
        state.portfolio[1].price*1.25
        state.portfolio[2].price*0.8
        state.portfolio[3].price*1.18
        state.portfolio[4].price*0.78
        state.portfolio_history.append(calculate_portfolio_value(state.portfolio))
        state.event_status = "Major Nations Clash in Global Cyber Standoff as Coordinated Attacks Hit Banking, Energy, and Telecom Networks."


    #conflict near strait of hormuz
    elif(rand == 4):
        state.portfolio[0].price*1.05
        state.portfolio[1].price*1.3
        state.portfolio[2].price*0.73
        state.portfolio[3].price*1.27
        state.portfolio[4].price*0.67
        state.portfolio_history.append(calculate_portfolio_value(state.portfolio))
        state.event_status = "Tensions Erupt at Strait of Hormuz as Naval Clash Disrupts Global Oil Shipping Routes."
   
    #major economic agreement between U.S and China
    elif(rand == 5):
        increment = 1.25
        for stock in state.portfolio:
            stock.price = stock.price * increment
        state.portfolio_history.append(calculate_portfolio_value(state.portfolio))
        state.event_status = "U.S. and China Sign Landmark Economic Pact Aimed at Lowering Tariffs and Stabilizing Global Trade."
    return index(state)

set_site_information(
    author="ashwinbm@udel.edu and danieleo@udel.edu",
    description="""Stonks the trading game""",
    sources=["Official Drafter Documentation only, Gemini"],
    planning=[""],
    links=[""]
)

start_server(State("", STOCKS,[0,0] ,STARTING_WALLET, ""))



