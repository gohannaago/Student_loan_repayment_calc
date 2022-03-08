# Header file with functions for calculator
#%%
def yn_to_bool(q_string):
    while 1:
        character = input(q_string)
        if character == 'y':
            return True
        elif character == 'n':
            return False
        else:
            print("Invalid input, please enter either y or n")

def calc(income, threshold, percentage):
    if income <= threshold: 
        return 0
    else:
        taxable = income - threshold
        return (taxable*(percentage/100))/12
        
# %%
# print(calc(25000, 21000, 6))