# ActTools
ActuarialTools for the modern general insurance actuary

## Library Structure

The library currently consists of the following modules:

- `actuarial_lib.core.math`: Core actuarial mathematics utilities.
- `actuarial_lib.ifrs17.risk_adjustment`: IFRS 17 specific actuarial logic for Risk Adjustment.

---

## API Reference

### Core Actuarial Math (`actuarial_lib.core.math`)

#### `discount_factor(rate, time)`
Calculates the discount factor for a given rate and time.
- **Args:**
  - `rate` (float): The annual interest rate (e.g., 0.05 for 5%).
  - `time` (float or np.array): The time in years.
- **Returns:** The discount factor (float or np.array).

#### `present_value(cashflows, times, rate)`
Calculates the present value of a series of cashflows.
- **Args:**
  - `cashflows` (np.array): The cashflow amounts.
  - `times` (np.array): The times at which cashflows occur.
  - `rate` (float): The annual interest rate.
- **Returns:** The present value (float).

#### `accumulated_value(amount, rate, time)`
Calculates the accumulated value of an amount over time.
- **Args:**
  - `amount` (float): The initial amount.
  - `rate` (float): The annual interest rate.
  - `time` (float): Time in years.
- **Returns:** Accumulated value (float).

---

### IFRS 17 Risk Adjustment (`actuarial_lib.ifrs17.risk_adjustment`)

#### `confidence_level_ra(cashflows, confidence_level=0.75)`
Calculates Risk Adjustment using the Confidence Level (Value at Risk - VaR) approach.
- **Args:**
  - `cashflows` (np.array): Simulated cashflow outcomes.
  - `confidence_level` (float): The target confidence level (default: 0.75 for 75th percentile).
- **Returns:** The Risk Adjustment, calculated as the difference between the percentile and the mean (float).

#### `t_var_ra(cashflows, confidence_level=0.75)`
Calculates Risk Adjustment using the Tail Value at Risk (TVaR) approach, sometimes known as Conditional Tail Expectation (CTE).
- **Args:**
  - `cashflows` (np.array): Simulated cashflow outcomes.
  - `confidence_level` (float): The target confidence level (default: 0.75).
- **Returns:** The Risk Adjustment, calculated as the difference between the mean of tail cashflows and the overall mean (float).

#### `cost_of_capital_ra(capital_requirements, discount_rates, coc_rate=0.06)`
Calculates Risk Adjustment using the Cost of Capital approach.
- **Args:**
  - `capital_requirements` (np.array): Projected capital requirements at each period.
  - `discount_rates` (np.array): Discount rates for each period.
  - `coc_rate` (float): The cost of capital rate (default: 0.06 for 6%).
- **Returns:** The Risk Adjustment (float).

## Installation
```bash
pip install .
```

## Development
To run tests, from the repository root:
```bash
$env:PYTHONPATH="src"
pytest
```
