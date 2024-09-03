import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("test streamlit")
st.write('test')

st.markdown("## my markdown")

code = '''
def hello():
    print("hello, st")
'''

run_btn = st.button("Show code")
if run_btn:
    st.markdown("code:")
    st.code(code, language='python')

cols = st.columns(2)
with cols[0]:
    age_inp = st.number_input("How old are you?", min_value=0, step=1, format="%d")
    st.markdown(f"Your age: {age_inp}")

with cols[1]:
    text_inp = st.text_input("input text:")
    text_token = "|".join(text_inp.split())
    st.markdown(f"tokenized text: {text_token}")

# df = pd.DataFrame({'test':[1,2], 'test2':['a','b']})
# st.dataframe(df)

# plot using matplotlib

# Title of the Streamlit app
st.title("Bar Chart from CSV")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Check if a file has been uploaded
if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    
    # Display the dataframe
    st.write("Data from CSV file:")
    st.write(df)
    
    # Check if 'id' and 'value' columns exist in the dataframe
    if 'id' in df.columns and 'value' in df.columns:
        show_button = st.button('Show Chart')
        if show_button:
            st.markdown("### Bar Chart")
            fig, ax = plt.subplots()
            ax.barh(df['id'], df['value'], color='skyblue')
            ax.set_xlabel('Value')
            ax.set_ylabel('ID')
            ax.set_title('Horizontal Bar Chart')

            st.pyplot(fig)

            st.markdown("### Line Chart")
            st.line_chart(df, x='id', y='value')
    else:
        st.error("CSV must contain 'id' and 'value' columns.")

