# World Happiness Analysis

## Project overview

This project explores how life evaluation varies across countries and how it changed from 2019 to 2025.

## Business question

How do life evaluation scores and country rankings differ, and how have they changed from 2019 to 2025? How do the explanatory factors compare across selected countries?

## Dashboard

The dashboard includes:
- A world map showing countries' life evaluation scores for the selected year.
- A line chart comparing the selected indicator across chosen countries from 2019 to 2025.
- A ranking table with countries' ranks, life evaluation scores, changes compared with 2019, and explanatory factors.
- Filters for year, country, and indicator to explore the data interactively.

https://public.tableau.com/app/profile/olena.vystavna/viz/HappinessAroundtheWorldTrendsandFactors/HappinessAroundtheWorldTrendsandFactors

## Data

Source: https://www.worldhappiness.report/data-sharing/ 
Note: The data used in this project covers 2019–2025. The World Happiness Report is based primarily on the Gallup World Poll and also uses other datasets.

## Methodology

1. Filtered and prepared World Happiness Report data for 2019–2025 using Python and Pandas.
2. Built an interactive Tableau dashboard with a world map, country trend lines and a ranking table.
3. Compared selected countries by life evaluation and explanatory factors.
4. Calculated the change in life evaluation compared with 2019.

## Tools

- Python (pandas)
- Tableau

## Repository structure

- `data/raw/` — raw input data
- `data/processed/` — aggregated data used by Tableau
- `scripts/` —  data checks and preparation
- `dashboard/` — Tableau workbook