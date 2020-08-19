import numpy as np

"""
Variable Creation - Distributions
Data Aggregation
"""
#Agents in Economy
number_of_agents = 1000
#Goods to buy from
number_of_goods = 100
#Create Random Distribution of Incomes and values of goods
incomes_data = np.random.normal(100, 20, number_of_agents)
valuations_data = np.random.normal(100, 20, number_of_agents)
"""
Functions:
wtp:
    input: price and agent valuation of the product
    return: agents that value the product
demand:
    input: price, valuation, and incomes
    return: sum of the all the agents who can afford
            multiplied by the agents who value it
profit:
    input: price, valuation
    output: price*those willing to pay for it

"""
def afford(p, incomes):
    """
    Makes a boolean list of the list of agents that can afford a product (True if they can, False if not)
    @inputparams::
    (float) p: price of goods
    (list) incomes: list of incomes of agents in economy
    @returnparams::
    (list, boolean) list of agents who can afford a good
    """
    return incomes>p
#Willingness to Pay for a product at price p
def wtp(p, valuations):
    """
    Boolean list of the list of the agents who value the product enough to buy it
    @inputparams::
    (float/integer) p: price of goods
    (list) valuations: list of evaluations from list of agents on the products
    (list) incomes: list of incomes of agents in economy
    @returnparams::
    (list, boolean) list of agents who value a good

    """
    return valuations>p
#Do they value it and can they afford it
def demand(p, valuations, incomes):
    """
    The calculated demand of a product with certain price (the sum of all the agents who can afford in addition to those who value the product)
    in essence: total amount of people "interested" in a product
    @inputparams::
    (float/integer) p: price of goods
    (list) valuations: list of evaluations from list of agents on the products
    (list) incomes: list of incomes of agents in economy
    @returnparams::
    (float) list of incomes who can afford a good
    """
    return np.sum(afford(p,incomes)*wtp(p,valuations))
def profit(p, valuations, incomes):
    """
    The calculated profit from a product (price*demand)
    @params::
    same as demand
    """
    return p*demand(p, valuations, incomes)

"""
Graphing the results
"""
import matplotlib.pyplot as plt

range_of_prices = np.linspace(0, 120, number_of_goods) #Create range of prices
plt.plot(range_of_prices, [profit(p, valuations_data, incomes_data) for p in range_of_prices], label='profit')
plt.legend()
plt.xlabel('$P$')
plt.ylabel('$\pi$')
plt.show()
