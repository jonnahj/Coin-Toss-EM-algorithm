draws_30 = []
for i in range(0,30):
    response = requests.get("https://24zl01u3ff.execute-api.us-west-1.amazonaws.com/beta")
    response = response.json()
    coin_flips = [int(i) for i in response["body"][1:59].split(",")]
    draws_30.append(coin_flips)
    
print(draws_30)

#Initial assumption theta_a = 0.60 and theta_b = 0.50
theta_a = 0.60
theta_b = 0.50
for i in range(0,10):
    coin_a_heads,coin_b_heads,coin_a_tails,coin_b_tails = 0,0,0,0
    #E-step
    for coin_flips in draws_30:
        a_numerator = pow(theta_a,coin_flips.count(1)) * pow((1-theta_a),(20 - coin_flips.count(1)))
        b_numerator = pow(theta_b,coin_flips.count(1)) * pow((1-theta_b),(20 - coin_flips.count(1)))
        probability_of_a = a_numerator/(a_numerator+b_numerator)
        probability_of_b = b_numerator/(a_numerator+b_numerator)
        
        coin_a_heads += probability_of_a * coin_flips.count(1)
        coin_b_heads += probability_of_b * coin_flips.count(1)
        
        coin_a_tails += probability_of_a * coin_flips.count(0)
        coin_b_tails += probability_of_b * coin_flips.count(0)
        
    #M-step    
    theta_a = coin_a_heads/(coin_a_heads+coin_a_tails)
    theta_b = coin_b_heads/(coin_b_heads+coin_b_tails)
    #total no. of flips by coin_a = no. of times it landed on heads + no. of times it landed on tails 
print("The thetas are:"+str(round(theta_a,2))+" and "+str(round(theta_b,2)))