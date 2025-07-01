import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Luca's Auto Detailing", layout="centered")

st.title("🚗 Luca's Auto Detailing")
st.subheader("Premium Mobile Car Detailing Services")

st.markdown("**Serving your area with top-quality interior & exterior detailing**")

st.image("https://images.unsplash.com/photo-1605296867304-46d5465a13f1", use_column_width=True)

st.markdown("### 📋 Our Services")
services = {
    "Exterior Wash": "$40",
    "Interior Detailing": "$60",
    "Full Detail (Interior + Exterior)": "$90",
    "Add-on: Pet Hair Removal": "+$15",
    "Add-on: Engine Bay Cleaning": "+$20"
}
for service, price in services.items():
    st.markdown(f"- **{service}** – {price}")

st.markdown("## 📅 Book an Appointment")

with st.form("booking_form", clear_on_submit=True):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    service = st.selectbox("Select a Service", list(services.keys()))
    date = st.date_input("Preferred Date")
    time = st.time_input("Preferred Time")
    submit = st.form_submit_button("Submit Appointment")

    if submit:
        new_data = pd.DataFrame([{
            "Name": name,
            "Email": email,
            "Phone": phone,
            "Service": service,
            "Date": date.strftime("%Y-%m-%d"),
            "Time": time.strftime("%H:%M"),
            "Submitted At": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }])

        try:
            existing = pd.read_csv("appointments.csv")
            updated = pd.concat([existing, new_data], ignore_index=True)
        except FileNotFoundError:
            updated = new_data

        updated.to_csv("appointments.csv", index=False)
        st.success("✅ Appointment submitted! We’ll contact you soon.")
