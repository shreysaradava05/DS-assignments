def get_final_price(price, discount):
    return price - price * discount / 100

def format_username(name):
    return name.strip().lower().replace(" ", "")

def split_bill(total_amount, num_people=2):
    if num_people <= 0:
        raise ValueError("Number of people must be greater than zero")
    return total_amount / num_people

print(get_final_price(1000, 10))
print(format_username(" Shrey Saidava "))
print(split_bill(900, 3))
