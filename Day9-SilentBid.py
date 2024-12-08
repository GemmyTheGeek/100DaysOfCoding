from os import system

bids = {}

while True:
    system('cls')
    name = input("Name (or 'exit' to stop): ")
    if name.lower() == 'exit':
        break
    bid = input("Bid: ")
    if bid.isdigit():
        bids[name] = int(bid)

if bids:
    winner = max(bids, key=bids.get)
    print(f"Winner: {winner} with ${bids[winner]}")
else:
    print("No bids placed.")
