

def replaceFaceCards(array):
    for i in range(len(array)):
        if array[i] == 'T':
            array[i] = '10'
        elif array[i] == 'J':
            array[i] = '11'
        elif array[i] == 'Q':
            array[i] = '12'
        elif array[i] == 'K':
            array[i] = '13'
        elif array[i] == 'A':
            array[i] = '14'

    return array

        #sort by card number, split into two arrays


#handArray looks like: ['0', '2c', 'As', Jh']
#function will find the best hand, and fill in all data in best_hand dictionary
def findBestHand(handArray):
    #make T-> 10, J-> 11, Q-> 12, K-> 13, twice through with A-> 1 and A-> 14
    #sort numbers
    #two arrays, one with card num, other with card suit (indices match)
    best_hand = {}
    best_hand['id'] = int(handArray[0])
    suits = []
    nums = []
    for card in handArray[1:]:
        suits.append(card[1])
        nums.append(card[0])
    nums = replaceFaceCards(nums) 
    nums = list(map(int, nums)) 
    nums.sort(reverse=True)
    best_hand['highest'] = nums[0]
    best_hand['hand'] = nums[1:]
    #checking for flush and straight
    for i in range(2):
        if (nums[0] == nums[1] + 1) and (nums[1] == nums[2] + 1):
            if (len(set(suits)) == 1):
                best_hand['best'] = 5 #means straight flush
                return best_hand
            else: #just a straight
                best_hand['best'] = 3
                return best_hand
        else:
            break
        if 14 in nums: #there is an ace, need to check for straight when A=1
            nums[0] = 1
            nums.sort(reverse=True)
            best_hand['highest'] = nums[0]
            best_hand['hand'] = nums
        else:
            break
        

    #checking for three of a kind
    if (len(set(nums)) == 1):
        best_hand['best'] = 4
        best_hand['high_triple'] = nums[0]

    #checking for flush
    elif (len(set(suits)) == 1):
        best_hand['best'] = 2

    #checking for pair
    elif (len(set(nums)) == 2):
        best_hand['best'] = 1
        if nums[0] in nums[1:]:
            best_hand['high_pair'] = nums[0]
        else:
            best_hand['high_pair'] = nums[1]

    #else high card is best
    else:
        best_hand['best'] = 0
    return best_hand
            
def tieComparisons(array, current_hand):
    original = array[0]
    if original['highest'] > current_hand['highest']:
        return array

    elif original['highest'] < current_hand['highest']:
        return [current_hand]

    #check tie for pair or three of kind
    if 'high_pair' in original:
        if original['high_pair'] > current_hand['high_pair']:
            return array
        elif original['high_pair'] < current_hand['high_pair']:
            return [current_hand]

    if 'high_triple' in original:
        if original['high_triple'] > current_hand['high_triple']:
            return array
        elif original['high_triple'] < current_hand['high_triple']:
            return [current_hand]
    


    if original['hand'][0] > current_hand['hand'][0]:
        return array

    elif original['hand'][0] < current_hand['hand'][0]:
        return [current_hand]
        
    else:
        if original['hand'][1] == current_hand['hand'][1]:
            array.append(current_hand)
            return array

        if original['hand'][1] > current_hand['hand'][1]:
            return array
        else:
            return [current_hand]
