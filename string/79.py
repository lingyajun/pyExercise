def count_word(str):
    wlist = str.split(' ')
    max1,min1 = 0, len(wlist[0])
    wmax, wmin = '',wlist[0]
    for w in wlist:
        length = len(w)
        if length > max1:
            max1 = length
            wmax = w
        if length < min1:
            min1 = length
            wmin = w
    return wmax, wmin, wlist
str1 = "Write a Java program to sort an array of given integers using Quick sort Algorithm.";  
large, small, wlist = count_word(str1)  
print("word list : " , wlist);   
print("Smallest word: " + small);  
print("Largest word: " + large); 


