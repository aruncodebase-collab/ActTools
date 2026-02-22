import numpy as np

def discount_factor(rate, time):
    """
    Calculate the discount factor for a given rate and time.
    
    Args:
        rate (float): The annual interest rate (e.g., 0.05 for 5%).
        time (float or np.array): The time in years.
        
    Returns:
        float or np.array: The discount factor.
    """
    return 1 / (1 + rate)**time

def present_value(cashflows, times, rate):
    """
    Calculate the present value of a series of cashflows.
    
    Args:
        cashflows (np.array): The cashflow amounts.
        times (np.array): The times at which cashflows occur.
        rate (float): The annual interest rate.
        
    Returns:
        float: The present value.
    """
    df = discount_factor(rate, times)
    return np.sum(cashflows * df)

def accumulated_value(amount, rate, time):
    """
    Calculate the accumulated value of an amount over time.
    """
    return amount * (1 + rate)**time
