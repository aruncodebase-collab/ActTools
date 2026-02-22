import numpy as np
import pytest
from actuarial_lib.core.math import discount_factor, present_value
from actuarial_lib.ifrs17.risk_adjustment import confidence_level_ra, cost_of_capital_ra

def test_discount_factor():
    assert discount_factor(0.05, 1) == 1 / 1.05
    assert discount_factor(0, 5) == 1.0

def test_present_value():
    cashflows = np.array([100, 100])
    times = np.array([1, 2])
    rate = 0.05
    expected = 100/1.05 + 100/(1.05**2)
    assert np.isclose(present_value(cashflows, times, rate), expected)

def test_confidence_level_ra():
    # Simulate some normally distributed cashflows
    np.random.seed(42)
    cashflows = np.random.normal(1000, 100, 10000)
    ra = confidence_level_ra(cashflows, 0.75)
    # 75th percentile for normal distribution is approx mean + 0.6745 * std
    assert np.isclose(ra, 0.6745 * 100, rtol=0.05)

def test_cost_of_capital_ra():
    capital = np.array([1000, 800, 600])
    rates = np.array([0.05, 0.05, 0.05])
    # CoC = 0.06
    # RA = (1000*0.06)/1 + (800*0.06)/1.05 + (600*0.06)/1.05^2
    expected = 60 + 48/1.05 + 36/(1.05**2)
    assert np.isclose(cost_of_capital_ra(capital, rates, 0.06), expected)
