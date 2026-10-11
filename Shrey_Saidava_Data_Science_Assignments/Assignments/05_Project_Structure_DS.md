# Assignment 1.5 — Professional Project Structure for Data Science
**Name:** Shrey Saidava | **Course:** Data Science

## 1. Spotify analysis project structure
```text
spotify-data-analysis/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── spotify_analysis.ipynb
├── scripts/
│   └── clean_data.py
├── dashboards/
├── reports/
├── tests/
├── .gitignore
├── requirements.txt
└── README.md
```

## 2. What belongs in each folder?
- `data/raw`: original data, kept unchanged.
- `data/processed`: cleaned data.
- `notebooks`: exploration and analysis notebooks.
- `scripts`: reusable Python programs.
- `dashboards`: dashboard files or instructions.
- `reports`: final charts and written findings.
- `tests`: basic checks for the code.

## 3. Example `.gitignore`
```text
__pycache__/
*.pyc
.ipynb_checkpoints/
.env
.DS_Store
```
I would normally avoid uploading private data, large raw files, passwords, and generated cache files.

## 4. README content
The README should explain the project goal, dataset source, steps to run the code, tools used, and key findings.

## 5. If the project used machine learning
I would add `models/` for model files if needed, `src/` for reusable training code, `configs/` for settings, and a section explaining model evaluation. I would also record how the model was trained and tested.
