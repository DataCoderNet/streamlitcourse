'''
Static Visualization
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("Static Visualizations with MatplotLib, Pandas and Seaborn")

#load the data
df = pd.read_csv("tips.csv")
st.dataframe(df.head())

##Questions
# 1.- Find number of Male and Female Distribution (pie and bar)
st.markdown('---')
with st.container():
    st.subheader("Number of Male and Female Distribution (pie and bar) - Matplotlib")
    value_counts = df["sex"].value_counts()

    #2 Column Layout
    c1, c2 = st.columns(2)

    # Draw Pie chart
    with c1:
        st.subheader("Pie chart")
        fig, ax = plt.subplots()
        ax.pie(value_counts, autopct="%0.1f%%", labels = ["Male", "Female"])
        st.pyplot(fig) ## Provide the figure

    #Draw Bar Plot
    with c2:
        st.subheader("Bar Chart")
        fig, ax = plt.subplots()
        ax.bar(value_counts.index, value_counts)
        st.pyplot(fig)

    #Put this in expander
    with st.expander("Click here to display value counts:"):
        st.dataframe(value_counts)





## Streamlit Widgets and charts

data_types = df.dtypes
cat_cols = tuple(data_types[data_types=="object"].index)
st.write(cat_cols)

st.markdown('---')
with st.container():
    feature = st.selectbox("Select the feature you want to distplay bar and pie chart", cat_cols)
    value_counts = df[feature].value_counts()


    #2 Column Layout
    c1, c2 = st.columns(2)

    # Draw Pie chart
    with c1:
        st.subheader("Pie chart")
        fig, ax = plt.subplots()
        ax.pie(value_counts, autopct="%0.1f%%", labels = value_counts.index)
        st.pyplot(fig) ## Provide the figure

    #Draw Bar Plot
    with c2:
        st.subheader("Bar Chart")
        fig, ax = plt.subplots()
        ax.bar(value_counts.index, value_counts)
        st.pyplot(fig)

    #Put this in expander
    with st.expander("Click here to display value counts:"):
        st.dataframe(value_counts)



# 2.- Find distribution of Male and Female spent (boxplot or kdeplot)

st.markdown('---')
with st.container():
    st.subheader("Distribution of Male and Female spent - Seaborn")

    # box, violin, kdeplot, histogram
    chart = ("box", "violin", "kdeplot", "histogram")

    chart_selection = st.selectbox("Select the chart type:", chart)
    
    fig, ax = plt.subplots()
    if chart_selection == "box":
        sns.boxplot(x="sex", y = "total_bill", data = df, ax=ax)
    elif chart_selection == "violin":
        sns.violinplot(x="sex", y = "total_bill", data = df, ax=ax)
    elif chart_selection == "kdeplot":
        sns.kdeplot(x=df["total_bill"], hue = df["sex"], ax=ax, shade=True)
    elif chart_selection == "histogram":
        sns.histplot(x="total_bill", hue = "sex", data=df, ax=ax)
    st.pyplot(fig)



# 3.- Find distribution of average total_bill across each day by male and female
# bar, area, line
st.markdown('---')
with st.container():
    st.subheader("Distribution of average total_bill across each day by male and female - Pandas")

    #1.- Include all categorical features
    #2.- Bar, area, line (selectbox)
    #3.- Stacked (radio)

    c1, c2, c3 = st.columns(3)

    with c1:
        group_cols = st.multiselect("Select the features", cat_cols, default=cat_cols[0])
        features_to_groupby = group_cols
        n_features = len(features_to_groupby)
    with c2:
        chart_type = st.selectbox("Select Chart Type", ("bar", "area", "line"))
    with c3:
        stack_option = st.radio("Stacked", ("Yes", "No"))
        if stack_option == "Yes":
            stacked = True
        else:
            stacked = False




    feature = ["total_bill"]
    select_cols = feature+features_to_groupby
    avg_total_bill = df[select_cols].groupby(features_to_groupby).mean()

    if n_features !=1:
        for i in range(n_features-1):
            avg_total_bill = avg_total_bill.unstack()

    avg_total_bill.fillna(0, inplace=True)

    #visualization
    fig, ax = plt.subplots()
    avg_total_bill.plot(kind=chart_type, ax = ax, stacked = stacked)
    ax.legend(loc="center left", bbox_to_anchor=(1.0, 0.5))
    ax.set_ylabel("Avg Total Bill")
    st.pyplot(fig)

    with st.expander("Click here to view values"):
        st.dataframe(avg_total_bill)

# 4.- Find the relation between total_bill and tip on time (Scatter plot)
st.markdown('---')
with st.container():
    st.subheader("Relation between total_bill and tip on time (Scatter plot) - Seaborn")

    hue_type = st.selectbox("Select the feature to hue", cat_cols)

    
    fig, ax =  plt.subplots()
    sns.scatterplot(x="total_bill", y="tip", hue=hue_type, ax=ax, data=df)
    st.pyplot(fig)



