cc = {
  "category" : {
    "Phone": 1,
    "Tablet": 2,
    "SIM card": 3,
    "Case": 4,
    "Charger": 5
  },
  "codes" : {
    "BPCM":1,
    "BPSH":2,
    "RPSS":3,
    "RPLL":4,
    "YPLS":5,
    "YPLL":6,
    "RTMS":7,
    "RTLM":8,
    "YTLM":9,
    "YTLL":10,
    "SMNO":11,
    "SMPG":12,
    "CSST":13,
    "CSLX":14,
    "CGCR":15,
    "CGHM":16
  },
  "description" : {
    "Compact": 1,
    "Compact": 1,
    "Clam Shell":1,
    "RoboPhone – 5-inch screen and 64GB memory":1,
    "RoboPhone – 6-inch screen and 256GB memory":1,
    "Y-Phone Standard – 6-inch screen and 64GB memory":1,
    "Y-Phone Deluxe – 6-inch screen and 256GB memory":1,
    "RoboTab – 8-inch screen and 64GB memory":2,
    "RoboTab – 10-inch screen and 128GB memory":2,
    "Y-Tab Standard – 10-inch screen and 128GB memory":2,
    "Y-Tab Deluxe – 10-inch screen and 256GB memory":2,
    "SIM Free (no SIM card purchased)":3,
    "Pay As You Go (SIM card purchased)":3,
    "Standard":4,
    "Luxury":4,
    "Car":5,
    "Home":5
  },
  "price" : {
    "29.99":"a",
    "49.99":"b",
    "199.99":"c",
    "499.99":"d",
    "549.99":"e",
    "649.99":"f",
    "149.99":"g",
    "299.99":"h",
    "499.99":"i",
    "599.99":"j",
    "0.00": "k",
    "50.00": "l",
    "19.99": "m",
    "15.99":"n"
  },


def categoryFunc():
  for i in cc:
    print(i)
  userC = input("Which category are you interested in? ")
  if userC == "Phone":
    print(description[0:6])
  userM = input("Which model are you interested in acquiring? (State the number in which the model appears on the list) ")
  if  1 <= int(userM) <= 6:
    print(description[int(userM)-1])
  else: print("wrong choice")

categoryFunc()