import streamlit as st
import pandas as pd

# Load CSV
df=pd.read_csv("user_purchase_dataset.csv")
st.title("🛍️ Surgical Products Catalog")

for i, row in df.head(10).iterrows():
    if pd.notna(row["Image"]) and row["Image"].startswith("http"):
        st.image(row["Image"], width=200)
    else:
        st.warning("No valid image available.")
        
    st.subheader(row["Title"])
    st.write(f"**Category:** {row['Category']}")
    st.write(f"**Price:** ${row['Price']}")
    st.markdown("---")
