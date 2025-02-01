```markdown
# Cross-Platform Coding Problem Search Engine

A search engine built with Flask and FastAPI that helps developers find coding problems across multiple platforms (LeetCode, CodeForces, and CodeChef) using TF-IDF based search.

## Features

- Search across multiple competitive programming platforms
- TF-IDF based relevance ranking
- Challenge name and direct link in results
- Clean and simple REST API endpoints
- Cross-platform compatibility
- Score-based result ranking

## Technology Stack

- Backend: Flask/FastAPI
- Frontend: React + TypeScript + Vite
- Search Algorithm: TF-IDF (Term Frequency-Inverse Document Frequency)

## Project Structure

```
project/
├── server/
│   ├── app.py                 # Main server file
│   └── data/                  # Data files
│       ├── leetcode/
│       ├── codeforces/
│       └── codechef/
├── client/
│   ├── src/
│   ├── package.json
│   └── vite.config.ts
└── requirements.txt
```

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Install frontend dependencies:
```bash
cd client
npm install
```

## Data Files Required

Each platform (leetcode, codeforces, codechef) needs the following files in its respective directory under `data/`:

- `vocab.txt`: Vocabulary terms
- `documents.txt`: Problem documents
- `inverted-index.txt`: Search index
- `question-links.txt`: Problem URLs
- `idf-values.txt`: IDF values for terms

## API Endpoints

- `GET /leetcode?query=<search_term>`: Search LeetCode problems
- `GET /codeforces?query=<search_term>`: Search CodeForces problems
- `GET /codechef?query=<search_term>`: Search CodeChef problems

## Running the Application

1. Start the backend server:
```bash
# For Flask
python app.py

# For FastAPI
uvicorn app:app --reload
```

2. Start the frontend development server:
```bash
cd client
npm run dev
```

## Search Algorithm

The search engine uses TF-IDF (Term Frequency-Inverse Document Frequency) to rank results:

1. Documents are preprocessed and indexed
2. Query terms are processed similarly
3. Results are ranked based on TF-IDF scores
4. Results include challenge names and direct links

## Development

- The backend is built with Flask/FastAPI
- Frontend uses React with TypeScript
- Vite is used for frontend tooling
- CORS is enabled for development

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```
