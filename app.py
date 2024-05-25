import streamlit as st

# Set up the app layout and title
st.set_page_config(page_title="Home Healthcare Services", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Services", "Book an Appointment", "Our Team", "Contact Us"])

# Home Page
if page == "Home":
    st.title("Welcome to Our Home Healthcare Services")
    st.write("""
        We provide top-notch home healthcare services to ensure the well-being of our clients in the comfort of their own homes.
        Our team of dedicated professionals is here to assist with a variety of healthcare needs.
    """)

# Services Page
elif page == "Services":
    st.title("Our Services")
    st.write("""
        - **Nursing Care**: Comprehensive nursing care including wound management, medication administration, and more.
        - **Physical Therapy**: Rehabilitation services to help improve mobility and physical function.
        - **Occupational Therapy**: Assistance with daily living activities to enhance independence.
        - **Personal Care**: Help with bathing, grooming, and other personal care tasks.
        - **Medical Social Services**: Support for emotional and social aspects of healthcare.
    """)

# Book an Appointment Page
elif page == "Book an Appointment":
    st.title("Book an Appointment")
    with st.form("appointment_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        service = st.selectbox("Service Required", ["Nursing Care", "Physical Therapy", "Occupational Therapy", "Personal Care", "Medical Social Services"])
        date = st.date_input("Preferred Date")
        time = st.time_input("Preferred Time")
        notes = st.text_area("Additional Notes")
        submitted = st.form_submit_button("Submit")

        if submitted:
            st.write("Thank you for booking an appointment. We will contact you shortly.")
            # Here you can add code to handle form submission, e.g., save to a database or send an email

# Our Team Page
elif page == "Our Team":
    st.title("Meet Our Team")
    st.write("""
        Our team consists of experienced and compassionate professionals dedicated to providing the best care possible.
    """)

    st.write("**John Doe, RN**\nRegistered Nurse")
    st.write("**Jane Smith, PT**\nPhysical Therapist")
    st.write("**Sarah Johnson, OT**\nOccupational Therapist")

# Contact Us Page
elif page == "Contact Us":
    st.title("Contact Us")
    st.write("If you have any questions or need further information, please contact us:")
    st.write("""
        **Address**: 1234 Healthcare St, Your City, Your State
        **Phone**: (123) 456-7890
        **Email**: info@homehealthcare.com
    """)

# Run the app with the following command in your terminal:
# streamlit run home_healthcare_app.py
