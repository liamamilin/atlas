# TECH STACK

## Language
- Frontend: TypeScript / TSX / React
- Backend: Python 3.11-compatible standard library service
- Data/build scripts: Node.js, Python

## Framework
- Frontend: Vite + React Router + Tailwind CSS
- Backend: local stdlib HTTP API
- State: SQLite + JSON/Markdown generated data

## Package Manager
- Frontend: npm
- Backend: Python environment with requirements.txt

## Install Command
```sh
cd atlas-web && npm ci
python3 -m pip install -r application-atlas-production-pack/requirements.txt
```

## Run Command
```sh
cd atlas-web && npm run dev -- --host 127.0.0.1 --port 5188
python3 application-atlas-production-pack/drafts_api.py --port 5199
```

## Test Command
```sh
python3 -m unittest discover -s application-atlas-production-pack/tests -q
cd atlas-web && npm run typecheck && npm test
cd atlas-web && npx playwright test
```

## Build Command
```sh
cd atlas-web && npm run build
```

## Lint Command
```sh
ruff check application-atlas-production-pack/<changed-python-files>
cd atlas-web && npm run typecheck
```
