def use_calculator(input_text):
    try:
        expression = input_text.split("calculator")[-1].strip()
        result = eval(expression)
        return f"{expression} = {result}"
    except Exception as e:
        return f"Error evaluating expression: {e}"