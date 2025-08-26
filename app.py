from streamlit.testing.v1 import AppTest

def test_calculator():
    at = AppTest.from_file("app.py")
    at.run()

    # Set values
    at.number_input[0].set_value(5.0)
    at.selectbox[0].set_value("Add")
    at.number_input[1].set_value(3.0)
    at.button[0].click()

    # Capture all outputs where result may appear
    output_values = [str(w.value) for w in at.write]

    # Assert that the expected result exists
    assert any("Result: 8.0" in v for v in output_values), \
        f"Expected result not found. Captured outputs: {output_values}"
