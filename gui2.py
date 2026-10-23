import streamlit as st
from emp_views import EmployeeManager

emp_instance = EmployeeManager()
tab1, tab2 = st.tabs(["ADD", "VIEW"])
with tab1:
    st.title("Add New Employee")
    name = st.text_input("Enter Employee Name")
    place = st.text_input("Enter Place")
    mobile = st.text_input("Enter Mobile Number")
    email = st.text_input("Enter Email")
    department = st.text_input("Enter Department")
    salary = st.text_input("Enter Salary")
    joining_date = st.text_input("Enter Joining Date(YYYY/MM/DD)")
    if st.button("Add New Employee"):
        emp_instance.post(name=name,place=place,mobile=mobile,email=email,department=department,salary=salary,joining_date=joining_date)
        st.success("Employee added successfully...!")
with tab2:
    st.title("View Employee Details")
    records = emp_instance.get()
    if records:
        st.table(records)
    else:
        st.warning("No records found")