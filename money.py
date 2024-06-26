def calculate_years(principal, interest, tax, desired):
    if desired == principal:
        return 0
    
    years = 0
    curr_sum = principal
    while curr_sum < desired:
        net_interest_gained = (curr_sum * interest) * (1.0 - tax)
        curr_sum += net_interest_gained
        years += 1
    return years

        
print(calculate_years(1000, 0.05, 0.18, 1100)) # should equal 3