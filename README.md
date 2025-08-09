# Auto-CV Service

A modular, scalable backend service for generating ATS-friendly CVs based on user-provided data. The project uses [FastAPI](https://fastapi.tiangolo.com) for the web framework and is structured to support additional services such as OCR and document generation.

## Features
- REST API built with FastAPI
- Service layer for CV generation and OCR (placeholders)
- Pydantic models for request/response validation
- Example test suite with pytest

## Getting Started

```bash
make install
auto-cv$ make run  # start development server on http://127.0.0.1:8000
```

## Project Structure

```
.
├── src/
│   └── autocv/
│       ├── api/            # API routers
│       ├── models/         # Pydantic models
│       ├── services/       # Business logic (CV generation, OCR)
│       └── main.py         # FastAPI application entry point
├── tests/                  # Unit tests
├── requirements.txt
└── Makefile
```

## Development

Run the test suite:

```bash
make test
```

Future enhancements will include real document generation and OCR integration.
