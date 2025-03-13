from fastapi import FastAPI
import random

app = FastAPI() 

# We Built two simple get endpoints
# side_hustles
# money_quotes


side_hustles = [
    "Freelancing - Start offering your skills online!",
    "Dropshipping - Sell without handling inventory!",
    "Stock Market - Invest and watch your money grow!",
    "Affiliate Marketing - Earn by promoting products!",
    "Crypto Trading - Buy and sell digital assets!",
    "Online Courses - Share your knowledge and earn!",
    "Print-on-Demand - Sell custom-designed products!",
    "Blogging - Create content and earn through ads and sponsorships!",
    "YouTube Channel - Monetize videos through ads and sponsorships!",
    "Social Media Management - Manage accounts for brands and influencers!",
    "App Development - Create mobile or web applications for bussinesses!"
]

money_quotes = [
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "Formal education will make you a living; self-education will make you a fortune. - Jim Rohn",
    "If you don't find a way to make money while you sleep, you will work until you die. - Warren Buffett",
    "Do not save what is left after spending, but spend what is left after saving. - Warren Buffett",
    "Money is a terrible master but an excellent servant. - P.T. Barnum",
    "You must gain control over your money, or the lack of it will forever control you. - Dave Ramsey",
    "Opportunities don't happen. You create them. - Chris Grosser",
    "The more you learn, the more you earn. - Warren Buffett",
    "Making money is art and working is art, and good business is the best art. - Andy Warhol",
    "Success is not in what you have, but who you are. - Bo Bennett",
    "Rich people have small TVs and big libraries; poor people have small libraries and big TVs. - Zig Ziglar",
    "An investment in knowledge pays the best interest. - Benjamin Franklin",
    "The secret to getting ahead is getting started. - Mark Twain",
    "Don't work for money; make it work for you. - Robert Kiyosaki",
    "A wise person should have money in their head, but not in their heart. - Jonathan Swift"
]


# Decorators

@app.get("/side_hustles")
def get_side_hustles():
# def get_side_hustles(apiKey: str):
    """Returns a random side hustle idea"""
    # if apiKey != "12345678901":
    # return {"Error": "Invalid API key"}
    return {"side_hustle": random.choice(side_hustles)}


@app.get("/money_quotes")
def get_money_quotes():
# def get_money_quotes(apiKey : str):
    """Returns a random money quote"""
    # if apiKey != "12345678901":
    # return {"Error": "Invalid API key"}
    return {"money_quote": random.choice(money_quotes)}
    


