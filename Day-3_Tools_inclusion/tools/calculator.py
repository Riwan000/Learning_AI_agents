def run(input_text: str) -> str:
    try:
        result = eval(input_text)
        return f"The result is {result}"
    except Exception as e:
        return f"Error in calculation: {e}"
