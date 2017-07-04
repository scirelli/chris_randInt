#!/usr/local/bin/python3
from random import randint, seed
from datetime import datetime

# final_tails = []
# for x in range(10):
# 	tails = ['']
# 	for x in range(10):
# 		coin = randint(0,2)
# 		coin = 'heads' if coin == 1 else 'tails'
# 		print('x: ', x, 'tails value at \'x\'\'', tails[x], '\'')
# 		tails.append(tails[x] + coin) #if we append coin, wont that give us both heads and tails as opposed to just tails?
# 	print('tails: ', tails);
# 	final_tails.append(tails[-1])

# print('final_tails: ', final_tails)

# tails:  ['', 'tails', 'tailstails', 'tailstailstails', 'tailstailstailstails', 'tailstailstailstailsheads', 'tailstailstailstailsheadstails', 'tailstailstailstailsheadstailstails', 'tailstailstailstailsheadstailstailsheads', 'tailstailstailstailsheadstailstailsheadsheads', 'tailstailstailstailsheadstailstailsheadsheadstails']
# tails:  ['', 'tails', 'tailsheads', 'tailsheadstails', 'tailsheadstailsheads', 'tailsheadstailsheadsheads', 'tailsheadstailsheadsheadstails', 'tailsheadstailsheadsheadstailsheads', 'tailsheadstailsheadsheadstailsheadstails', 'tailsheadstailsheadsheadstailsheadstailsheads', 'tailsheadstailsheadsheadstailsheadstailsheadstails']
# tails:  ['', 'heads', 'headsheads', 'headsheadstails', 'headsheadstailsheads', 'headsheadstailsheadstails', 'headsheadstailsheadstailstails', 'headsheadstailsheadstailstailsheads', 'headsheadstailsheadstailstailsheadsheads', 'headsheadstailsheadstailstailsheadsheadsheads', 'headsheadstailsheadstailstailsheadsheadsheadstails']
# tails:  ['', 'heads', 'headstails', 'headstailstails', 'headstailstailstails', 'headstailstailstailstails', 'headstailstailstailstailstails', 'headstailstailstailstailstailsheads', 'headstailstailstailstailstailsheadstails', 'headstailstailstailstailstailsheadstailstails', 'headstailstailstailstailstailsheadstailstailsheads']
# tails:  ['', 'tails', 'tailsheads', 'tailsheadsheads', 'tailsheadsheadstails', 'tailsheadsheadstailstails', 'tailsheadsheadstailstailsheads', 'tailsheadsheadstailstailsheadstails', 'tailsheadsheadstailstailsheadstailstails', 'tailsheadsheadstailstailsheadstailstailstails', 'tailsheadsheadstailstailsheadstailstailstailsheads']
# tails:  ['', 'tails', 'tailsheads', 'tailsheadstails', 'tailsheadstailstails', 'tailsheadstailstailstails', 'tailsheadstailstailstailstails', 'tailsheadstailstailstailstailsheads', 'tailsheadstailstailstailstailsheadstails', 'tailsheadstailstailstailstailsheadstailsheads', 'tailsheadstailstailstailstailsheadstailsheadstails']
# tails:  ['', 'heads', 'headstails', 'headstailsheads', 'headstailsheadstails', 'headstailsheadstailsheads', 'headstailsheadstailsheadstails', 'headstailsheadstailsheadstailstails', 'headstailsheadstailsheadstailstailstails', 'headstailsheadstailsheadstailstailstailstails', 'headstailsheadstailsheadstailstailstailstailstails']
# tails:  ['', 'heads', 'headstails', 'headstailstails', 'headstailstailsheads', 'headstailstailsheadstails', 'headstailstailsheadstailstails', 'headstailstailsheadstailstailsheads', 'headstailstailsheadstailstailsheadstails', 'headstailstailsheadstailstailsheadstailstails', 'headstailstailsheadstailstailsheadstailstailstails']
# tails:  ['', 'tails', 'tailstails', 'tailstailsheads', 'tailstailsheadstails', 'tailstailsheadstailstails', 'tailstailsheadstailstailstails', 'tailstailsheadstailstailstailstails', 'tailstailsheadstailstailstailstailstails', 'tailstailsheadstailstailstailstailstailsheads', 'tailstailsheadstailstailstailstailstailsheadstails']
# tails:  ['', 'tails', 'tailstails', 'tailstailstails', 'tailstailstailstails', 'tailstailstailstailstails', 'tailstailstailstailstailstails', 'tailstailstailstailstailstailstails', 'tailstailstailstailstailstailstailstails', 'tailstailstailstailstailstailstailstailsheads', 'tailstailstailstailstailstailstailstailsheadstails']
# final_tails:  ['tailstailstailstailsheadstailstailsheadsheadstails', 'tailsheadstailsheadsheadstailsheadstailsheadstails', 'headsheadstailsheadstailstailsheadsheadsheadstails', 'headstailstailstailstailstailsheadstailstailsheads', 'tailsheadsheadstailstailsheadstailstailstailsheads', 'tailsheadstailstailstailstailsheadstailsheadstails', 'headstailsheadstailsheadstailstailstailstailstails', 'headstailstailsheadstailstailsheadstailstailstails', 'tailstailsheadstailstailstailstailstailsheadstails', 'tailstailstailstailstailstailstailstailsheadstails']

# TAILS = 1

# final_tails = []
# for x in range(10):
# 	tails = []
# 	tailsCount = 0
# 	for x in range(10):
# 		coin = randint(0,2)
# 		if(coin == TAILS):
# 			tailsCount += 1
# 		coin = 'heads' if coin == 1 else 'tails'

# 		print('x: ', x, 'tailsCount: \'', tailsCount, '\'')
# 		tails.append(tailsCount)
# 	print('tails: ', tails);
# 	final_tails.append(tails[-1])

# print('final_tails: ', final_tails)



# TAILS = 1

# final_tails = []
# for x in range(10):
# 	tailsCount = 0
# 	for x in range(10):
# 		coin = randint(0,2)
# 		if(coin == TAILS):
# 			tailsCount += 1

# 	final_tails.append(tailsCount)

# print('final_tails: ', final_tails)

TAILS = 1
HEADS = 0
TOTAL_FLIPS = 1000000
SEED_EVERY = 100

def game():
    seed(datetime.now())
    count = 0
    for _ in range(TOTAL_FLIPS):
        flip = randint(0,1)
        if flip == TAILS:
            count += 1
        else:
            count -= 1
    
        if _ % SEED_EVERY == 0:
            seed(datetime.now())
    
    if count < 0:
        print('Heads biased: ', count)
    elif count == 0:
        print('No biased')
    else:
        print('Tails biased: ', count)
        
    return count
        
while game() != 0:
    continue
else: 
    print('Perfect game!')
