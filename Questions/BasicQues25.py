#WAF to convert USD to INR. (USD is the parameter)

def usd_to_inr(usd):
    exchange_rate = 90
    return usd * exchange_rate
print(usd_to_inr(100))
