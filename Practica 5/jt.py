def wordsOfFreqency(words, freq):

    _ = words[0]
    a = 0
    j = 0
    while x != (freq):
        for i in words:
            if i == test_words:
                x += 1
                print(i)
        else:
            j = x
            test_words = words[j]
        
    
            

if __name__ == '__main__':

 
    user_input = input()
    words = user_input.split()
    
    
 

    
    

    freq = int(input())
    

    returnedStrs = wordsOfFreqency(words, freq)
    print(returnedStrs)