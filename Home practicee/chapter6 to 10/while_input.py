prompt = "Tell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
active=True
while active:
    message = input(prompt)
    if message=='quit':
        active=False
    if message=='quit': #or condition
        break
    else:
        print(message)