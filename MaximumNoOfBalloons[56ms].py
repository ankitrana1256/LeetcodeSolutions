class Solution(object):
    def maxNumberOfBalloons(text):
        flag = True
        counter = True
        count = 0
        a = {}
        for i in text:
            if i not in a:
                a[i] = text.count(i)
                
        word = "balloon"
        word2 = "".join(list(set(word)))
        while flag:
            try:
                for i in word2:
                    c = word.count(i)
                    if a[i] >= c and c != 0:
                        print(word2,i,a[i], c)
                        a[i] -= c
                    else:
                        print(word2,i,a[i], c, "Failed")
                        flag = False
                        counter = False
                        break   
                print('\n')
                if counter:
                    count += 1
            except:
                flag = False
                
        return count
    
text = "balloonballoon"
a = Solution.maxNumberOfBalloons(text)
print(a)