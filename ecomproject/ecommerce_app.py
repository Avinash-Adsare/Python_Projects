import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title("E-commerce Data Analysis App")
    st.sidebar.title("Upload Your Dataset")

    # Upload file section
    uploaded_file = st.sidebar.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                data = pd.read_csv(uploaded_file)
            else:
                data = pd.read_excel(uploaded_file)

            st.sidebar.success("File uploaded successfully!")

            st.subheader("Dataset Overview")
            st.dataframe(data.head())

            # Display basic information
            st.subheader("Basic Information")
            st.write("**Shape of the dataset:**", data.shape)
            st.write("**Columns in the dataset:**", list(data.columns))
            st.write("**Missing Values:**", data.isnull().sum().sum())

            # Generate summary statistics
            st.subheader("Summary Statistics")
            st.write(data.describe())

            # Visualizations
            st.subheader("Visualizations")

            if 'Gender' in data.columns:
                st.write("### Gender Distribution")
                fig, ax = plt.subplots()
                sns.countplot(data=data, x='Gender', palette='Set2', ax=ax)
                st.pyplot(fig)

            if 'Age' in data.columns:
                st.write("### Age Distribution")
                fig, ax = plt.subplots()
                sns.countplot(data=data, x='Age', palette='viridis', ax=ax, order=data['Age'].value_counts().index)
                st.pyplot(fig)

            if 'Purchase' in data.columns:
                st.write("### Purchase Analysis")
                if 'Gender' in data.columns:
                    purchase_gender = data.groupby('Gender')['Purchase'].sum()
                    fig, ax = plt.subplots()
                    purchase_gender.plot(kind='bar', color=['skyblue', 'orange'], ax=ax)
                    ax.set_title("Total Purchase by Gender")
                    ax.set_ylabel("Purchase Amount")
                    st.pyplot(fig)

                if 'Age' in data.columns:
                    purchase_age = data.groupby('Age')['Purchase'].sum()
                    fig, ax = plt.subplots()
                    purchase_age.plot(kind='bar', color='lightcoral', ax=ax)
                    ax.set_title("Total Purchase by Age Group")
                    ax.set_ylabel("Purchase Amount")
                    st.pyplot(fig)

        except Exception as e:
            st.error(f"Error loading the file: {e}")
    else:
        st.info("Please upload a dataset to get started.")

if __name__ == "__main__":
    main()
