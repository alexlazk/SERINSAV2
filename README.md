# Simple Dashboard Setup

This repository contains:

- `SIS_db_profile_es.json`: JSON description of the existing SQL Server database.
- `Evaluacion Posibles KPIs (2).xlsx`: Spreadsheet with potential KPIs that can be built using the current data.

The initial code uses Python and [Streamlit](https://streamlit.io/) for a very basic dashboard.

## Prerequisites

- Python 3.10+
- A SQL Server instance with credentials.
- The Python dependencies from `requirements.txt`.

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Copy `.env.example` to `.env` and fill in your database connection details.

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

This will open a local web page with placeholders for KPIs.

## Replit

You can fork this repository on Replit and run the same commands in the shell pane to install dependencies and launch the app. Replit automatically creates a virtual environment for you.

