pattern='123'
text='ab123cabaabcabaadrycycrbtrabaav123yvcutctababrfyabaa'
p,t,i=len(pattern),len(text),0
for i in range(0,t-p+1): 
    j=0
    while(j<p):        
        if(pattern[j]==text[i]):
            i,j=i+1,j+1
        else:
            break
    if(j==p):
        print("Valid Shifts:",i-j)
    i=i-j+1
