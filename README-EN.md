# Comic Prompt Generator

A Streamlit application for generating detailed prompts for 4-panel comic creation using AI image generators.

## Features

- Interactive UI for designing 4-panel comics
- Detailed prompt generation for AI image models
- Reference image support
- Customizable comic style profiles
- Support for text placement, sound effects, and transitions

## Installation

1. Install [uv](https://github.com/astral-sh/uv) package manager
2. Clone this repository
3. Create a virtual environment and install dependencies:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -e .
   ```

## Usage

Run the application with:
```bash
streamlit run src/app.py
```

## Project Structure

```
comic-prompt-gen/
├── src/
│   └── app.py
├── pyproject.toml
└── README.md
```

## Development

This project uses:
- Python 3.9+
- Streamlit for the web interface
- Ruff for linting
- uv for package management 