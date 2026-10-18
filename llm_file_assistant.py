from fs_tools import read_file, list_files, write_file, search_in_file
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENAI_API_KEY")
)

read_file_tool = {
    "type": "function",
    "name": "read_file",
    "description": "Read a resume and return its content and metadata",
    "parameters": {
        "type": "object",
        "properties": {
            "filepath": {"type": "string", "description": "Path to the resume file."}
        },
        "required": ["filepath"],
    },
}

list_files_tool = {
    "type": "function",
    "name": "list_files",
    "description": "List files in a directory and return their metadata.",
    "parameters": {
        "type": "object",
        "properties": {
            "directory": {
                "type": "string",
                "description": "Directory containing the files.",
            },
            "extension": {
                "type": "string",
                "description": "Optional file extension filter such as .pdf, .docx, or .txt.",
            },
        },
        "required": ["directory"],
    },
}

write_file_tool = {
    "type": "function",
    "name": "write_file",
    "description": "Write text content to a file. Creates the file and parent directories if they do not exist.",
    "parameters": {
        "type": "object",
        "properties": {
            "filepath": {"type": "string", "description": "Path of the file to write."},
            "content": {
                "type": "string",
                "description": "Text content to write to the file.",
            },
        },
        "required": ["filepath", "content"],
    },
}

search_in_file_tool = {
    "type": "function",
    "name": "search_in_file",
    "description": "Search for a keyword in a file and return matching context.",
    "parameters": {
        "type": "object",
        "properties": {
            "filepath": {
                "type": "string",
                "description": "Path to the file to search.",
            },
            "keyword": {
                "type": "string",
                "description": "Keyword or text to search for.",
            },
        },
        "required": ["filepath", "keyword"],
    },
}

tools = [
    read_file_tool,
    list_files_tool,
    write_file_tool,
    search_in_file_tool,
]


tool_functions = {
    "read_file": read_file,
    "list_files": list_files,
    "write_file": write_file,
    "search_in_file": search_in_file,
}


def ask_llm(prompt: str):
    input_items = [
        {
            "role": "user",
            "content": prompt,
        }
    ]

    while True:
        response = client.responses.create(
            model="openai/gpt-5-mini",
            input=input_items,
            max_output_tokens=1000,
            instructions="""
You are a file assistant working with files in the local filesystem.

You have access to tools for listing, reading, searching, and writing files.

Rules:
- When the user asks about files or resumes, use the available file tools instead of asking the user to upload files.
- The resumes are stored in the "resumes" directory unless the user specifies another directory.
- For "find resumes mentioning X", first list the files in the resumes directory, then search the relevant files for X.
- For "read all resumes", first list the files, then read each resume.
- For "create a summary file", read the requested resume, create the summary, and use write_file to save it.
- Use the tools yourself whenever the requested information can be obtained from the local files.
- Do not ask the user for the directory if "resumes" is already implied by the request.
""",
            tools=tools,
        )

        tool_calls = [item for item in response.output if item.type == "function_call"]

        if not tool_calls:
            return response.output_text

        # Add the COMPLETE model output to the next request
        input_items.extend(response.output)

        for item in tool_calls:
            arguments = json.loads(item.arguments)

            function = tool_functions[item.name]

            result = function(**arguments)

            input_items.append(
                {
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": str(result),
                }
            )
