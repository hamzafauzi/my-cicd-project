# CI/CD Pipeline from Scratch — FastAPI + Docker + GitHub Actions + Render

![CI](https://github.com/hamzafauzi/my-cicd-project/actions/workflows/ci.yml/badge.svg)

A small but complete **continuous integration and continuous deployment (CI/CD) pipeline**, built from the ground up. A single `git push` automatically tests the code, packages it into a Docker container, and deploys it live to the internet — with no manual steps in between.

The application itself is intentionally simple (a tiny web API). The point of this project is the **automation around it**.

**Live demo:** https://my-cicd-project-7i66.onrender.com
- Health check: [`/health`](https://my-cicd-project-7i66.onrender.com/health)
- Example endpoint: [`/add?a=5&b=7`](https://my-cicd-project-7i66.onrender.com/add?a=5&b=7)
- Interactive API docs: [`/docs`](https://my-cicd-project-7i66.onrender.com/docs)

> Note: the live demo is hosted on a free tier that sleeps after inactivity. The first request after an idle period may take 30–50 seconds to wake up.

## How the pipeline works

```
   git push
      │
      ▼
┌─────────────┐     ┌──────────────────────┐     ┌────────────────────┐
│   GitHub    │────▶│   GitHub Actions      │────▶│       Render        │
│ (source of  │     │   (CI)                │     │       (CD)          │
│  truth)     │     │   • lint / install    │     │   • builds Docker   │
│             │     │   • run pytest        │     │     image           │
│             │     │   • pass / fail gate  │     │   • deploys live    │
└─────────────┘     └──────────────────────┘     └────────────────────┘
                                                            │
                                                            ▼
                                                   Live public URL
```

1. **Push** — code is pushed to the `main` branch on GitHub.
2. **Continuous Integration (GitHub Actions)** — a fresh Ubuntu runner checks out the code, installs dependencies, and runs the automated test suite. If any test fails, the run is marked failed.
3. **Continuous Deployment (Render)** — Render watches the repository and, on every push, rebuilds the application from the `Dockerfile` and redeploys it automatically.

## Tech stack

| Layer | Tool | Why |
|-------|------|-----|
| Application | **FastAPI** (Python) | Minimal, modern web framework with automatic interactive docs |
| Server | **Uvicorn** | ASGI server that runs the FastAPI app |
| Testing | **pytest** | Runs the automated test suite |
| Containerization | **Docker** | Packages the app + Python + dependencies into one portable image |
| CI | **GitHub Actions** | Runs tests automatically on every push |
| CD / Hosting | **Render** | Auto-builds from the Dockerfile and deploys on every push |

## Project structure

```
my-cicd-project/
├── app/
│   ├── __init__.py
│   └── main.py              # FastAPI app and endpoints
├── tests/
│   ├── __init__.py
│   └── test_main.py         # automated tests for the endpoints
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions CI pipeline
├── Dockerfile               # builds the container image
├── .dockerignore
├── .gitignore
├── requirements.txt
└── README.md
```

## Running it locally

Clone the repository and enter it:

```bash
git clone https://github.com/hamzafauzi/my-cicd-project.git
cd my-cicd-project
```

### Option A — run directly with Python

```bash
python -m venv venv
source venv/bin/activate        # on Windows: venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open http://127.0.0.1:8000/docs

### Option B — run with Docker

```bash
docker build -t my-cicd-app .
docker run -p 8000:8000 my-cicd-app
```

Then open http://127.0.0.1:8000/docs

## Running the tests

```bash
pytest
```

The same test suite runs automatically on every push via GitHub Actions.

## What I learned building this

- The difference between an **image** (a frozen, layered filesystem) and a **container** (a running instance of an image), and why Docker solves the "works on my machine" problem.
- How **port mapping** connects a port on the host to a port inside a container.
- How **GitHub Actions** runs a workflow on a clean virtual machine on every push, acting as an automated safety net.
- How **continuous deployment** ties the whole chain together so that pushing code is the only manual action required.
