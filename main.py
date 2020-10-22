category = ["Phone", "Tablet", "SIM card", "Case", "Charger"]
codes = ["BPCM", "BPSH", "RPSS", "RPLL", "YPLS", "YPLL", "RTMS","RTLM", "YTLM","YTLL","SMNO","SMPG","CSST","CSLX","CGCR","CGHM"]
description = ["Compact","Clam Shell","RoboPhone – 5-inch screen and 64GB memory", "RoboPhone – 6-inch screen and 256GB memory", "Y-Phone Standard – 6-inch screen and 64GB memory", "Y-Phone Deluxe – 6-inch screen and 256GB memory", "RoboTab – 8-inch screen and 64GB memory", "RoboTab – 10-inch screen and 128GB memory", "Y-Tab Standard – 10-inch screen and 128GB memory", "Y-Tab Deluxe – 10-inch screen and 256GB memory", "SIM Free (no SIM card purchased)", "Pay As You Go (SIM card purchased)", "Standard", "Luxury", "Car", "Home"]
price = ["29.99", "49.99", "199.99","499.99","549.99","649.99","149.99","299.99","499.99","599.99","0.00","50.00","19.99","15.99"]

def categoryFunc():
  for i in category:
    print(i)
  userC = input("Which category are you interested in? ")
  if userC == "Phone":
    print(description[0:6])
  userM = input("Which model are you interested in acquiring? (State the number in which the model appears on the list) ")
  if  1 <= int(userM) <= 6:
    print(description[int(userM)-1])
  else: print("wrong choice")

categoryFunc()