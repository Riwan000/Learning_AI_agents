import tiktoken

def trim_messages(messages, max_tokens=3000):
    enc = tiktoken.encoding_for_model("gpt-3.5-turbo")
    total_tokens = 0
    trimmed = []
    for message in reversed(messages):
        tokens = len(enc.encode(message["content"]))
        if total_tokens + tokens > max_tokens:
            break
        total_tokens += tokens
        trimmed.insert(0, message)
    return trimmed
