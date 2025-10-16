# CORD-19 Research Dataset Analysis

## Overview
This project analyzes the CORD-19 metadata.csv (COVID-19 papers). Uses Pandas for exploration/cleaning, Matplotlib/Seaborn/WordCloud for viz, and Streamlit for an interactive app.

## Learning Objectives Met
- Loaded/explored real-world data.
- Cleaned missing values/dates.
- Visualized trends (pubs over time, journals, words).
- Built simple Streamlit app with sliders/dropdowns.

## Files
- analysis.ipynb: Step-by-step analysis and code.
- app.py: Streamlit app (run with `streamlit run app.py`).
- sample_metadata.csv: Small sample of cleaned data (full on Kaggle due to size).
- pubs_by_year.png, top_journals.png, wordcloud_titles.png, sources_pie.png: Visualizations.
- requirements.txt: Install deps with `pip install -r requirements.txt`.

## How to Run
1. Clone repo: `git clone https://github.com/yourusername/Frameworks_Assignment.git`
2. Install: `pip install -r requirements.txt`
3. Run analysis: Open analysis.ipynb in Jupyter/Colab.
4. Run app: `streamlit run app.py` (opens browser with interactive explorer).

## Key Findings
- Publications spiked in 2020 (over 100k papers in sample trends).
- Top journals: PLoS One, BMJ, medRxiv.
- Common title words: virus, patients, infection, study.
- Sources: Mostly PMC and medRxiv.
- Challenges: Handled large file by sampling; date parsing errors fixed with `errors='coerce'`.
- Reflection: Learned data cleaning (e.g., datetime conversion) and Streamlit widgets. Basics like word frequency were eye-opening for text analysis.

## Data Source
Kaggle: https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge
(Used metadata.csv; sampled for repo.)
