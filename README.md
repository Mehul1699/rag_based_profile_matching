A resume RAG system that uses embeddings, vector search, and LLMs to match candidates with job descriptions.

# LLM File Assistant

A command-line file assistant that uses an LLM to interact with files and resumes through natural-language instructions.

The assistant can list files, read files, search within files, and create/write files using tools exposed to the LLM.

## Features

- List files from a directory
- Filter files by extension
- Read resume files
- Extract text from PDF, DOCX, and TXT files
- Search for keywords inside files
- Create and write files
- Use an LLM to decide which file operation to perform
- Support multiple tool calls for a single user request
- Interact with the assistant through the terminal

## Supported File Types

The project currently supports:

- `.pdf`
- `.docx`
- `.txt`

## Project Structure

```text
llm-file-assistant/
│
├── main.py
├── llm_file_assistant.py
├── file_tools.py
├── requirements.txt
├── README.md
├── .env
│
└── resumes/
    ├── resume1.pdf
    ├── resume2.docx
    └── resume3.txt
