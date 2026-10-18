from llm_file_assistant import ask_llm

while True:
    prompt = input("You: ")

    if prompt.lower() == "exit":
        break

    result = ask_llm(prompt)

    print("Assistant:", result)