import unittest
from unittest.mock import patch
import streamlit as st

# The calculator logic to test
def calculate(num1, operation, num2):
    if operation == "Add":
        return num1 + num2
    elif operation == "Subtract":
        return num1 - num2
    elif operation == "Multiply":
        return num1 * num2
    elif operation == "Divide":
        return num1 / num2 if num2 != 0 else "Error: Division by zero"

class TestCalculatorApp(unittest.TestCase):
    @patch('streamlit.number_input')
    @patch('streamlit.selectbox')
    @patch('streamlit.button')
    @patch('streamlit.write')
    def test_addition(self, mock_write, mock_button, mock_selectbox, mock_number_input):
        # Mock inputs
        mock_number_input.side_effect = [5.0, 3.0]  # num1 = 5.0, num2 = 3.0
        mock_selectbox.return_value = "Add"
        mock_button.return_value = True

        # Simulate calculator logic
        result = calculate(5.0, "Add", 3.0)
        
        # Test the result
        self.assertEqual(result, 8.0)
        mock_write.assert_called_with("Result: 8.0")

    @patch('streamlit.number_input')
    @patch('streamlit.selectbox')
    @patch('streamlit.button')
    @patch('streamlit.write')
    def test_subtraction(self, mock_write, mock_button, mock_selectbox, mock_number_input):
        # Mock inputs
        mock_number_input.side_effect = [5.0, 3.0]  # num1 = 5.0, num2 = 3.0
        mock_selectbox.return_value = "Subtract"
        mock_button.return_value = True

        # Simulate calculator logic
        result = calculate(5.0, "Subtract", 3.0)
        
        # Test the result
        self.assertEqual(result, 2.0)
        mock_write.assert_called_with("Result: 2.0")

    @patch('streamlit.number_input')
    @patch('streamlit.selectbox')
    @patch('streamlit.button')
    @patch('streamlit.write')
    def test_multiplication(self, mock_write, mock_button, mock_selectbox, mock_number_input):
        # Mock inputs
        mock_number_input.side_effect = [5.0, 3.0]  # num1 = 5.0, num2 = 3.0
        mock_selectbox.return_value = "Multiply"
        mock_button.return_value = True

        # Simulate calculator logic
        result = calculate(5.0, "Multiply", 3.0)
        
        # Test the result
        self.assertEqual(result, 15.0)
        mock_write.assert_called_with("Result: 15.0")

    @patch('streamlit.number_input')
    @patch('streamlit.selectbox')
    @patch('streamlit.button')
    @patch('streamlit.write')
    def test_division(self, mock_write, mock_button, mock_selectbox, mock_number_input):
        # Mock inputs
        mock_number_input.side_effect = [6.0, 2.0]  # num1 = 6.0, num2 = 2.0
        mock_selectbox.return_value = "Divide"
        mock_button.return_value = True

        # Simulate calculator logic
        result = calculate(6.0, "Divide", 2.0)
        
        # Test the result
        self.assertEqual(result, 3.0)
        mock_write.assert_called_with("Result: 3.0")

    @patch('streamlit.number_input')
    @patch('streamlit.selectbox')
    @patch('streamlit.button')
    @patch('streamlit.write')
    def test_division_by_zero(self, mock_write, mock_button, mock_selectbox, mock_number_input):
        # Mock inputs
        mock_number_input.side_effect = [6.0, 0.0]  # num1 = 6.0, num2 = 0.0
        mock_selectbox.return_value = "Divide"
        mock_button.return_value = True

        # Simulate calculator logic
        result = calculate(6.0, "Divide", 0.0)
        
        # Test the result
        self.assertEqual(result, "Error: Division by zero")
        mock_write.assert_called_with("Result: Error: Division by zero")

if __name__ == '__main__':
    unittest.main()