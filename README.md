# Automated EDA Profiler — Square 1 AI starter

**Part of [Square 1 AI](https://square1-tutor.vercel.app) · Data Science · Project 1.**

✅ **Data included.** The dataset is committed in [`dataset/`](dataset/) and is the **same standardized dataset every learner uses** — so results are comparable. It is 100% synthetic and Square 1-owned (no third-party or personal data). You can also download it as a single file from the project page on Square 1.

To run the commands below, copy the files into `data/` (`mkdir -p data && cp -r dataset/* data/`) or point the commands straight at `dataset/`.

MIT licensed — fork it, build on it, put it in your portfolio.

---

# Automated EDA Profiler — starter

Starter scaffold for the Square 1 AI **Data Science · Project 1**. Build a tool that profiles any CSV and generates a shareable HTML report.

## Setup
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Get the data
Download `ecommerce_transactions.csv` from your project page (Resources → Dataset) into `data/`.

## Your task
Three tests define the contract. Run them — they fail until you implement the stubs in `profiler/profiler.py`:
```bash
pytest -q
```
Then build the report and run:
```bash
python -m profiler.cli data/ecommerce_transactions.csv --out report.html
```

## What "done" looks like
- `pytest` passes.
- `report.html` covers: overview, data-quality (missing/duplicates), numeric distributions + outliers, categorical top-values, correlation heatmap.
- README updated with a screenshot and your design notes.

See the full brief, rubric, and references on your Square 1 project page. MIT licensed — fork freely.
