"""write your code in method currency_exchange"""
def currency_exchange():
    euro=int(input("How many eruos are you exchanging?"))
    rate=float(input('What is the exchange rate?'))
    dollar=euro*rate/100
    print('%d euros at an exchange rate of %.2f is %.2f U.S. dollars.'%(euro,rate,dollar)) 
    return 

