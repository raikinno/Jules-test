# CLAUDE.md

This file provides guidance for AI assistants working with this repository.

## Project Overview

A minimal Python utility that fetches one year of S&P 500 historical data from Yahoo Finance and renders a candlestick chart saved as a PNG file.

## Repository Structure

```
Jules-test/
├── generate_chart.py   # Single entry-point script
├── requirements.txt    # Python dependencies (yfinance, mplfinance)
├── .gitignore          # Ignores *.png (generated output)
└── CLAUDE.md           # This file
```

No subdirectories, no package structure, no test suite.

## Tech Stack

- **Language:** Python 3
- **`yfinance`** — fetches OHLCV data from Yahoo Finance
- **`mplfinance`** — renders candlestick charts with volume panels

## Setup & Running

```bash
# Install dependencies (virtualenv recommended)
pip install -r requirements.txt

# Run the script
python3 generate_chart.py
```

**Output:** `sp500_chart.png` in the working directory (git-ignored). A success message is printed in Japanese; an error message is printed if no market data is returned (e.g., weekend/holiday).

## Key Conventions

- **Single-function design:** all logic lives in `generate_sp500_chart()` with the standard `if __name__ == "__main__"` guard.
- **Snake_case** for all identifiers.
- **Inline comments in Japanese** — preserve this style when adding code.
- **No classes, no modules** — keep the flat, single-file structure unless the scope genuinely requires splitting.
- **No tests** — the project has none; do not add a test framework unless explicitly asked.
- **No linting config** — follow PEP 8 manually; do not introduce `.flake8`, `black`, or similar tooling without being asked.

## Chart Parameters (generate_chart.py)

| Parameter | Value | Notes |
|-----------|-------|-------|
| Ticker | `^GSPC` | S&P 500 index |
| Window | 365 days back from `datetime.date.today()` | Fixed look-back |
| Chart type | `candle` | mplfinance candlestick |
| Style | `charles` | Built-in mplfinance theme |
| Output | `sp500_chart.png` | Overwritten on each run |

## Development Branch

Active development happens on `claude/claude-md-docs-J8gcV`. The remote is `raikinno/Jules-test` on GitHub.

## Common Tasks

**Changing the ticker:** update `ticker_symbol` in `generate_sp500_chart()`.

**Changing the time window:** update the `datetime.timedelta(days=365)` offset and/or the `start_date`/`end_date` variables.

**Changing the output filename:** update the `savefig` argument in `mpf.plot(...)`.

**Adding a new chart style:** pass a different string to the `style` parameter — run `mpf.available_styles()` to list options.
