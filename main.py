from myStack import myStack
import numpy as np

arr = np.random.randint(0, 100, 30)
st = myStack()
for i in arr:
    st.insert(i)
print(arr)
st.printStack()