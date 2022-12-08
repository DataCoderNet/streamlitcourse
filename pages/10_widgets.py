'''
Widgets
'''
import os
import pandas as pd
import streamlit as st
import datetime

data = pd.read_csv('tips.csv')

def display_data_random(df):
    '''display data function'''
    sample = df.sample(5)
    return sample

## BUTTON WIDGET
st.subheader("st.button()")
st.markdown ("##### Display Random 4 Rows")
st.caption("Click on the button below to display the rows")
button = st.button("Display Random 5 rows")
st.write("button status ", button)
if button:
    sample1 = display_data_random(data)
    st.dataframe(sample1)

## CHECKBOX
st.markdown('''---''')
st.subheader("st.checkbox()")
agree = st.checkbox("I agree to terms and conditions") # Return boolean value
st.write("checkbox status ", agree)


### MULTIPLE CHECKBOX
with st.container():
    st.info("What technologies you know? ")

    python = st.checkbox("Python")
    datascience = st.checkbox("Data Science")
    ai_ml = st.checkbox("AI / ML")
    android = st.checkbox("Android")
    react = st.checkbox("React JS")
    java = st.checkbox("Core Java")
    javascript = st.checkbox("Javascript")

    tech_button = st.button("Submit")
    if tech_button:
        tech_dict = {
            'Python': python,
            'Data Science': datascience,
            "ML": ai_ml,
            "Android": android,
            "React" : react,
            "Java": java,
            "Javascript": javascript
        }

        st.json(tech_dict)


## RADIO BUTTON
st.markdown('''---''')
st.subheader("st.radio()")
radio_button = st.radio("What is your favorite color?", ("White", "Black", "Pink", "Red", "Green"))

st.write("Your favorite color is: ", radio_button)


## SELECT BOX
st.markdown('''---''')
st.subheader("st.selectbox()")
select_box = st.selectbox("What skill you want to learn most?", ("Java", "Python", "C", "Javascript", "HTML"))
st.write("You selected :", select_box)


### MULTI SELECT BOX
st.markdown('''---''')
st.subheader("st.multiselect()")
options = st.multiselect("What kind of movies you like?", ["Comedy", "Action", "Sci-fi", "Drama", "Romance"])
st.write("You selected these options: ", options)


### SLIDER
st.markdown('''---''')
st.subheader("st.slider()")
loan = st.slider("What is loan amount you are looking for?", 0, 100000, 1000, 10000)
st.write("The loan amount is: ", loan)


### TEXT INPUT / NUMBER INPUT / TEXT AREA
st.markdown('''---''')
st.subheader("st.text_input()")

with st.container():
    name = st.text_input("Please your name")
    age = st.number_input("Please your age", min_value=0, max_value=150, value=25, step=1)
    dob = st.date_input("Select date of birth")
    describe = st.text_area("Please describe yourself: ", height=150)

    submit_button = st.button("submit")
    if submit_button:
        info = {
            "Name": name,
            "Age": age,
            "Date of Birth": dob,
            "Description": describe

        }
        st.json(info)


### FILE UPLOAD

st.markdown('''---''')
st.subheader("st.file_uploader()")
uploaded_file = st.file_uploader("Choose a file to upload: ")
save_button = st.button("Save file")
if save_button:
    if uploaded_file is not None:
        with open(os.path.join("./save_folder", uploaded_file.name), mode="wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success("File uploaded successfully")
    else:
        st.warning("Please select the file you want to upload")

### DATE
st.markdown('''---''')
today = datetime.date.today()
today_date = st.date_input('Cual es tu cumple : ', today)
#st.success('tu cumple es : `%s` felicidades ...' % (today_date))
st.success(f'tu cumple es: {today_date} felicidades...') 