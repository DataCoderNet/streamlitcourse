'''
Text Elements
'''
import streamlit as st

st.title("This is the title")
st.header("This is a header")
st.subheader("This is a subheader")
st.caption("This is a caption")
st.code('''
    # Sample of python code

    import numpy as np
    np.random.randn(1,10)
    print("Hello World")
''', language='python')
st.latex('''
    a + ar + ar^2 + \cdots + a r^{n-1} + sum_{k}
''')
