import streamlit as st

st.set_page_config(
    page_title="Employee Management System",
    page_icon="👨‍💼",
    layout="wide"
)

if "employees" not in st.session_state:
    st.session_state.employees = []

employees = st.session_state.employees

st.title("👨‍💼 Employee Management System")
st.write("Manage Your Employee Records Easily")

st.sidebar.title("Dashboard")

menu = st.sidebar.selectbox(
    "Select Operation",
    [
        "Add Employee",
        "View Employees",
        "Search Employee",
        "Update Employee",
        "Delete Employee"
    ]
)

if menu == "Add Employee":

    st.header("➕ Add Employee")

    emp_id = st.text_input("Employee ID")
    name = st.text_input("Employee Name")
    salary = st.number_input("Employee Salary", min_value=0.0)

    if st.button("Add Employee"):

        if not emp_id or not name:
            st.error("Please enter Employee ID and Name")

        elif any(e["ID"] == emp_id for e in employees):
            st.error("Employee ID already exists")

        else:
            employees.append({
                "ID": emp_id,
                "Name": name,
                "Salary": salary
            })

            st.success("Employee Added Successfully!")

elif menu == "View Employees":

    st.header("📋 Employee Details")

    if employees:
        st.dataframe(employees, use_container_width=True)
    else:
        st.info("No Employees Found")

elif menu == "Search Employee":

    st.header("🔍 Search Employee")

    search_id = st.text_input("Enter Employee ID")

    if st.button("Search"):

        result = next(
            (e for e in employees if e["ID"] == search_id),
            None
        )

        if result:
            st.success("Employee Found!")
            st.write(result)
        else:
            st.error("Employee Not Found")

elif menu == "Update Employee":

    st.header("✏️ Update Employee")

    update_id = st.text_input("Enter Employee ID")

    employee = next(
        (e for e in employees if e["ID"] == update_id),
        None
    )

    if employee:

        new_name = st.text_input(
            "New Name",
            value=employee["Name"]
        )

        new_salary = st.number_input(
            "New Salary",
            min_value=0.0,
            value=float(employee["Salary"])
        )

        if st.button("Update Employee"):

            employee["Name"] = new_name
            employee["Salary"] = new_salary

            st.success("Employee Updated Successfully!")

    else:
        st.info("Enter an existing Employee ID")

elif menu == "Delete Employee":

    st.header("🗑️ Delete Employee")

    delete_id = st.text_input("Enter Employee ID")

    if st.button("Delete Employee"):

        employee = next(
            (e for e in employees if e["ID"] == delete_id),
            None
        )

        if employee:
            employees.remove(employee)
            st.success("Employee Deleted Successfully!")
        else:
            st.error("Employee Not Found")
