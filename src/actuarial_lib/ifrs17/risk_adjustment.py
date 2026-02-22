import numpy as np
from scipy.stats import norm

def confidence_level_ra(cashflows, confidence_level=0.75):
    """
    Calculate Risk Adjustment using the Confidence Level (VaR) approach.
    
    Args:
        cashflows (np.array): Simulated cashflow outcomes.
        confidence_level (float): The target confidence level (e.g., 0.75 for 75th percentile).
        
    Returns:
        float: The Risk Adjustment (Difference between percentile and mean).
    """
    mean_cf = np.mean(cashflows)
    percentile_cf = np.percentile(cashflows, confidence_level * 100)
    return percentile_cf - mean_cf

def t_var_ra(cashflows, confidence_level=0.75):
    """
    Calculate Risk Adjustment using the Tail VaR (TVaR) approach.
    """
    var = np.percentile(cashflows, confidence_level * 100)
    tail_cashflows = cashflows[cashflows >= var]
    tvar = np.mean(tail_cashflows)
    mean_cf = np.mean(cashflows)
    return tvar - mean_cf

def cost_of_capital_ra(capital_requirements, discount_rates, coc_rate=0.06):
    """
    Calculate Risk Adjustment using the Cost of Capital approach.
    
    Args:
        capital_requirements (np.array): Projected capital requirements at each period.
        discount_rates (np.array): Discount rates for each period.
        coc_rate (float): The cost of capital rate (e.g., 0.06 for 6%).
        
    Returns:
        float: The Risk Adjustment.
    """
    ra = 0
    for t, (k, r) in enumerate(zip(capital_requirements, discount_rates)):
        # Cost of capital for period t
        cost = k * coc_rate
        # Discount the cost back to present value
        ra += cost / (1 + r)**t
    return ra
