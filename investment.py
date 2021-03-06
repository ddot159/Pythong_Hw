def calculate_apr(principal, interest_rate, years):
    """
    Calculates the interest rate with years
    """
    i=0
    output = 0
    
    if principal <= 0:
        return False
    elif interest_rate <= 0:
        return False
    elif years <=0:
        return False
    else:
        while i < years:
            i = i + 1    
            output = (float(principal)*(1 + float(interest_rate)))**float(years)
            return output
    
