from  art import logo
print(logo)

def highest_bidder (bid_dictionary):
    highest_bid = 0
    winner=""
    for bidder in bid_dictionary :
        bid_amount = bid_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} and bid is {highest_bid}")

cont = True
dictionary = {}
while (cont == 1):
    print("hello")
    name = input("what is your name? : ")
    bid = int(input("\nwhat is your bid: $"))
    dictionary[name] = bid
    ask=(input("any one else to bid : yes / no : ")).lower()
    if ask=='no':
        cont = False
        highest_bidder(dictionary)

    elif ask == 'yes' :
        cont = True
