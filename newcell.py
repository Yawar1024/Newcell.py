import streamlit as st

# Set the title of the app
st.title('Simple Calculator')

# Define the options for the dropdown menu
operation = st.selectbox('Select Operation', ['Add', 'Subtract', 'Multiply', 'Divide'])

# Input fields for numbers
num1 = st.number_input('Enter the first number', value=0)
num2 = st.number_input('Enter the second number', value=0)

# Perform the calculation based on the selected operation
if st.button('Calculate'):
    if operation == 'Add':
        result = num1 + num2
    elif operation == 'Subtract':
        result = num1 - num2
    elif operation == 'Multiply':
        result = num1 * num2
    elif operation == 'Divide':
        if num2 != 0:
            result = num1 / num2
        else:
            result = 'Error: Division by zero'
    
    # Display the result
    st.write('Result:', result)

