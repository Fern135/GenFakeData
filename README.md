# GenFakeData

A REST API that generates fake data on demand. Available in two implementations — **Node.js (Express)** and **Python (Django)** — both exposing the same endpoints.

---

## Requirements

### To run either version
- **Python 3.10+** — needed to run the root `run.py` launcher

### Node.js version
- **Node.js 18+**
- **npm**

### Python version
- **Python 3.10–3.13** (3.14 may have package compatibility issues)
- `venv` module (included with Python by default)

---

## Quick Start

From the **root** of the project, run:

```bash
python3 run.py        # macOS / Linux
python run.py         # Windows
```

You'll be prompted to choose a version:

```
which version would you want to run (node, python?)
```

Type `node` or `python` and press Enter.

The launcher will automatically:
- **Node** — install `node_modules` if missing, then start the server
- **Python** — create a `venv` and install dependencies if missing, then start the server

---

## Running Manually

### Node.js

```bash
cd node
npm install           # first time only
npm run dev           # development (auto-restarts on file changes)
npm run production    # production
```

Server starts at `http://localhost:3000`

### Python

```bash
cd python
python3 run.py        # macOS / Linux
python run.py         # Windows
```

This handles venv creation, dependency installation, and starts gunicorn with uvicorn workers automatically.

Or step by step:

```bash
cd python
bash scripts/setup.sh          # macOS / Linux — creates venv and installs deps
scripts\setup.bat              # Windows
venv/bin/python manage.py runserver   # simple dev server (no gunicorn needed)
```

Server starts at `http://127.0.0.1:8000`

---

## API Endpoints

Both versions expose the same routes. The `count` parameter is optional and defaults to `10`.

| Endpoint | Description |
|---|---|
| `GET /api/users` | Generate fake users |
| `GET /api/users/<count>` | Generate `count` fake users |
| `GET /api/products` | Generate fake products |
| `GET /api/products/<count>` | Generate `count` fake products |
| `GET /api/companies` | Generate fake companies |
| `GET /api/companies/<count>` | Generate `count` fake companies |
| `GET /api/credit-cards` | Generate fake credit cards |
| `GET /api/credit-cards/<count>` | Generate `count` fake credit cards |
| `GET /api/jobs` | Generate fake job listings |
| `GET /api/jobs/<count>` | Generate `count` fake job listings |
| `GET /api/text-contents` | Generate fake lorem paragraphs |
| `GET /api/text-contents/<count>` | Generate `count` fake paragraphs |
| `GET /api/help` | List all available routes *(Node only)* |
| `GET /ping` | Health check — returns `pong` *(Node only)* |

### Example response — `/api/users/2`

```json
{
  "message": [
    { "id": 2, "name": "Jane Smith", "email": "jsmith@gmail.com", "phone": "555-123-4567" },
    { "id": 3, "name": "John Doe",   "email": "jdoe@yahoo.com",   "phone": "555-987-6543" }
  ]
}
```

---

## Rate Limiting

Both versions enforce a **10 requests/second per IP** limit using a sliding-window approach. Exceeding the limit returns:

```json
{ "error": "rate limit exceeded", "limit": 10, "window": "1s" }
```

with HTTP status `429`.

| Version | File to edit | Constant |
|---|---|---|
| Node.js | [node/lib/rateLimit.js](node/lib/rateLimit.js) | `RATE_LIMIT` |
| Python | [python/fakerGen/middleware.py](python/fakerGen/middleware.py) | `RATE_LIMIT` |

Both also respect the `X-Forwarded-For` header so clients behind a proxy or load balancer are identified by their real IP.

---

## Load Tester

A load tester is included at the root of the project. It hits all 6 endpoints concurrently and doubles the `count` each round until a request takes longer than 60 seconds.

```bash
python3 tester.py     # server must already be running
```

Make sure the server is running before starting the tester. It targets `http://127.0.0.1:8000` by default (Python). To test the Node server, change `BASE_URL` in [tester.py](tester.py) to `http://localhost:3000`.

---

## Project Structure

```
GenFakeData/
├── run.py                  # Root launcher — prompts for node or python
├── tester.py               # Async load tester
│
├── node/
│   ├── index.js            # Express app entry point
│   ├── routes/
│   │   └── dataRoutes.js   # Route definitions
│   ├── controllers/
│   │   └── dataController.js
│   ├── lib/
│   │   ├── DataGenerator.js
│   │   └── util.js
│   └── package.json
│
└── python/
    ├── run.py              # Python launcher (handles venv + gunicorn)
    ├── requirements.txt
    ├── scripts/
    │   ├── setup.sh        # venv setup — macOS / Linux
    │   └── setup.bat       # venv setup — Windows
    ├── fakerGen/           # Django app
    │   ├── views.py        # Data generation logic
    │   ├── urls.py         # URL patterns
    │   └── middleware.py   # Rate limiting
    └── genFakeData/        # Django project config
        └── settings.py
```
