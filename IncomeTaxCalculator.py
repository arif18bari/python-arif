def calculate_income_tax(income):
    tax = 0.0

    # No tax for income up to 3.5 lac
    if income <= 350000:
        return tax

    # Tax for the next 1 lac at 5%
    income -= 350000
    if income <= 100000:
        tax += income * 0.05
        return tax
    else:
        tax += 100000 * 0.05
        income -= 100000

    # Tax for the next 4 lac at 10%
    if income <= 400000:
        tax += income * 0.10
        return tax
    else:
        tax += 400000 * 0.10
        income -= 400000

    # Tax for the next 5 lac at 15%
    if income <= 500000:
        tax += income * 0.15
        return tax
    else:
        tax += 500000 * 0.15
        income -= 500000

    # Tax for the next 5 lac at 20%
    if income <= 500000:
        tax += income * 0.20
        return tax
    else:
        tax += 500000 * 0.20
        income -= 500000

    # Tax for the next 20 lac at 25%
    if income <= 2000000:
        tax += income * 0.25
        return tax
    else:
        tax += 2000000 * 0.25
        income -= 2000000

    # Tax for the remaining income at 30%
    tax += income * 0.30

    return tax

# Example usage
income = 10000000  # Example income
tax = calculate_income_tax(income)
print(f"The income tax for an income of {income} is: {tax:.2f}")
