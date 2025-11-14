def rayan(text):
    text.lower()
    count=0;
    con=0;
    arr="aeiou"
    for ch in text:
        if ch.isalpha():
            if ch in arr:
                count+=1
            else:
                con+=1
    return count,con
text="rAyanpinto"
c,n=rayan(text)
print(c,n)