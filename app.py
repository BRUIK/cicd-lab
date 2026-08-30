# app.py
import streamlit as st
from datetime import date
from late_fee import calculate_late_fee

st.set_page_config(page_title="Library Late Fee Calculator", page_icon="📚")

st.title("📚 Library Late Fee Calculator")
st.write("Enter the due date and return date to calculate the late fee.")

due_date = st.date_input("Due Date", value=date.today())
return_date = st.date_input("Return Date", value=date.today())

if st.button("Calculate Fine"):
    if return_date < due_date:
        st.error("Return date cannot be before the due date.")
    else:
        days_late = (return_date - due_date).days
        fee = calculate_late_fee(days_late)

        st.write(f"### Days late: {days_late}")
        st.success(f"### Fine: Rs. {fee}")

        if fee == 500:
            st.warning("Maximum fine reached (capped at Rs. 500).")
