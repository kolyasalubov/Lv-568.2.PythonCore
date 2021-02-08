def reverse(st):      
    st = list(st.split(" "))    
    while "" in st:        
        st.remove("")
    st.reverse()       
    st = (' '.join(st))      
    return st