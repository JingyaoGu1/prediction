import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map


def clean_experience(x):
    if x ==  'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)


def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Post grad'
    return 'Less than a Bachelors'


@st.cache_data
def load_data():
    df = pd.read_csv("./stack-overflow-developer-survey-2023/processed_survey_data.csv")
    return df

df = load_data()

def show_explore_page():
    st.title("Explore Software Engineer Salaries")

    st.write(
        """
    ### Stack Overflow Developer Survey 2023
    """
    )

    data = df["Country"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.write("""#### Number of Data from different countries""")

    st.pyplot(fig1)
    
    st.write(
        """
    #### Mean Salary Based On Country
    """
    )

    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write(
        """
    #### Mean Salary Based On Experience
    """
    )

    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)

    st.write("#### Salary Distribution by Education Level")
    fig2, ax2 = plt.subplots()
    df.boxplot(column='Salary', by='EdLevel', ax=ax2)
    plt.xticks(rotation=45)
    st.pyplot(fig2)

    st.write("#### Average Salary by Country and Education Level (Heat Map)")
    data = df.pivot_table(index='Country', columns='EdLevel', values='Salary', aggfunc='mean')
    fig3, ax3 = plt.subplots(figsize=(12, 8))
    sns.heatmap(data, annot=True, fmt=".0f", linewidths=.5, ax=ax3)
    st.pyplot(fig3)

    st.write("#### Experience Distribution Among Respondents")
    fig4, ax4 = plt.subplots()
    df['YearsCodePro'].hist(bins=20, ax=ax4)
    st.pyplot(fig4)

    st.write("#### Top 10 Highest Paying Countries")
    top_countries = df.groupby('Country')['Salary'].mean().nlargest(10)
    st.bar_chart(top_countries)

