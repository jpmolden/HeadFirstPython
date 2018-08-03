word = "bottles"

    # loop beer_num from 99, 98,..., 1.
for beer_num in range(99,0,-1):
    print(beer_num, word, "of beer on the wall")
    print(beer_num, word, "of beer")
    print("Take one down")
    print("Pass it around")
        # final line if last beer :D
    if beer_num == 1:
        print("No more bottles of beer on the wall")
    else:
        # if not the last beer
        new_num = beer_num - 1
        # changes word to bottle if going from 2 to 1 beers
        if new_num == 1:
            word = "bottle"
        # final line
        print(new_num, word, "of beer on the wall")
        
    print()
    
        
    

    
