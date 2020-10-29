#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def common10():
    from collections import Counter
    a=[]
    # Extract data in purpose
    for sentence in file['purpose']:
        a.append(sentence)
    b=pd.DataFrame(a)
    # Turn into one string
    b=b[0].str.cat(sep=' ')
    # Find the 10 most common words
    common=Counter(b.split()).most_common()[0:10]
    print(common)
    

if __name__ == "__main__":
    common10()

