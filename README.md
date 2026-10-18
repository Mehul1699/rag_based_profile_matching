# Resume RAG-Based Profile Matching System

## Overview

This project uses Retrieval-Augmented Generation (RAG) techniques and semantic similarity to match candidate resumes with job descriptions. It retrieves relevant resume sections, identifies matching skills, and ranks candidates based on their suitability for a specific job role.

The system supports multiple resume formats and allows users to select from predefined job descriptions.

## Features

- Extracts resume content from PDF, DOCX, and TXT files.
- Splits resumes into meaningful chunks for retrieval.
- Generates embeddings using OpenRouter's embedding API.
- Stores and searches resume embeddings using ChromaDB.
- Matches resumes against job descriptions using semantic similarity and skill coverage.
- Identifies matched and missing skills.
- Ranks candidates using a configurable matching score.
- Applies optional eligibility criteria, including mandatory skills.
- Saves candidate matching results as JSON.
- Uses a Jupyter Notebook for experiments and evaluation.

## Technologies Used

- **Python** — Core programming language
- **OpenRouter API** — Text embedding generation
- **OpenAI Python SDK** — API client
- **ChromaDB** — Vector database and semantic retrieval
- **Sentence/Document Processing** — PDF and DOCX text extraction
- **Pandas** — Data analysis
- **Jupyter Notebook** — Experimentation and evaluation
- **python-dotenv** — Environment variable management

## Project Structure

```text
rag_based_profile_matching/
├── resumes/                  # Resume files
├── job_descriptions/         # Predefined job descriptions
├── chroma_db/                # Local vector database (generated)
├── resume_rag.py             # Resume processing and indexing
├── job_matcher.py            # Candidate matching and ranking
├── experiments.ipynb         # Experiments and evaluation
├── job_match_results.json    # Matching results
├── .env                      # API key (not committed)
├── .env.example              # Example environment configuration
├── .gitignore
└── README.md
```

## Requirements

- Python 3.10 or a compatible version
- An OpenRouter API key
- Internet access for embedding generation
- Required Python libraries

## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd rag_based_profile_matching
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

Install the libraries used by the project:

```bash
pip install openai python-dotenv chromadb pypdf python-docx pandas jupyter ipykernel
```

If your code uses any additional libraries, install those as well.

### 4. Configure the API key

Create a `.env` file in the project root:

```text
OPENAI_API_KEY=your_openrouter_api_key_here
```

The project uses OpenRouter with the `openai/text-embedding-3-small` embedding model.

**Security:** Never commit your `.env` file or expose your API key publicly.

### 5. Add resumes and job descriptions

Place the permitted resume files in the `resumes/` directory. Supported formats are PDF, DOCX, and TXT.

Place the five job description text files in the `job_descriptions/` directory.

## Running the Project

### Step 1: Index resumes

Run the resume processing and indexing script:

```bash
python resume_rag.py
```

This step should extract resume text, create chunks, generate embeddings, and store them in ChromaDB. If indexing is exposed through a function rather than the script's main execution, call that function as configured in the code.

### Step 2: Match candidates

Run:

```bash
python job_matcher.py
```

Select a job description from the available options. The system then retrieves relevant resume chunks, calculates matching scores, and ranks eligible candidates.

### Step 3: View the results

The matching results are saved in:

```text
job_match_results.json
```

The results include candidate names, resume paths, match scores, semantic similarity, matched skills, missing skills, eligibility, and retrieved resume excerpts.

## Matching Methodology

The matching pipeline consists of the following steps:

1. **Resume processing:** Extract text from supported resume formats.
2. **Chunking:** Divide resume content into smaller sections for retrieval.
3. **Embedding generation:** Convert resume chunks and job descriptions into vector representations.
4. **Semantic retrieval:** Retrieve resume chunks that are semantically similar to the selected job description.
5. **Skill matching:** Identify relevant skills present in the job description and candidate resume content.
6. **Candidate aggregation:** Combine retrieved chunks belonging to the same candidate.
7. **Scoring and ranking:** Calculate a combined score using semantic similarity and skill coverage.
8. **Eligibility filtering:** Apply any configured mandatory-skill or experience requirements.
9. **Result generation:** Save the ranked candidates and matching evidence to JSON.

The current scoring configuration uses semantic similarity and skill coverage, with weights defined in `job_matcher.py`. The weights and eligibility rules can be adjusted for experimentation.

## Experiments and Evaluation

The `experiments.ipynb` notebook is used to analyze the dataset and evaluate the matching system.

Experiments can include:

- Counting indexed resumes and resume chunks.
- Measuring matching execution time.
- Comparing candidate rankings across different job descriptions.
- Inspecting matched and missing skills.
- Applying score thresholds to select candidates.
- Calculating Precision@10 and Recall@10 using relevance labels.

A score threshold, such as 70%, can be used to explore automatic candidate selection. However, a high matching score does not automatically establish that a candidate is genuinely relevant.

For meaningful precision and recall measurements, relevance labels should ideally be established through manual review independently of the model's scores. If fewer than ten candidates are returned, the evaluation should clearly state the actual number of returned candidates.

## Limitations

- Matching quality depends on resume extraction, chunking, and skill detection.
- Semantic similarity does not guarantee that a candidate meets every job requirement.
- Results depend on the resumes available in the database and the number of chunks retrieved.
- The skill dictionary may not recognize every synonym or variation of a skill.
- Embedding generation requires API access and may introduce latency or usage costs.
- Candidate rankings should support, not replace, human review.

## Future Improvements

- Improve skill extraction using NLP.
- Add synonym and related-skill matching.
- Improve experience and mandatory-requirement validation.
- Compare alternative scoring weights and retrieval settings.
- Add evaluation against manually reviewed relevance labels.
- Build a simple web interface for uploading resumes and selecting job descriptions.

## Responsible Use

Use resumes only when authorized to process them. Candidate rankings should be reviewed by a human, and the system should not be used as the sole basis for employment decisions.

## Author

Developed as a project on Retrieval-Augmented Generation and resume-to-job matching.