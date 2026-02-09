---
mode: 'agent'
description: 'Run the complete Crypto Watchtower pipeline: fetch → filter → analyze → visualize → build dashboard → deploy'
tools: ['terminalLastCommand', 'editFiles', 'codebase']
---

# Run Complete Pipeline

Execute the full Crypto Watchtower pipeline from data fetch to deployment.

## Pipeline Steps

### Step 1: Fetch Data (The Scout)
```bash
curl -s "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&sparkline=false" -o crypto_raw.json
```

### Step 2: Filter Volatile Coins (The Editor)
```bash
jq '[.[] | select(.price_change_percentage_24h > 5 or .price_change_percentage_24h < -5) | {name, symbol, current_price, price_change_percentage_24h, market_cap}]' crypto_raw.json > volatile_movers.json
```

### Step 3: Generate Analysis Report
Create and run a Python script that:
- Loads `volatile_movers.json`
- Generates `volatility_report.json` with statistics
- Creates `daily_brief.txt` with human-readable summary

### Step 4: Create Visualization (The Artist)
Create and run `generate_chart.py` to produce `market_chart.png`

### Step 5: Build Dashboard (The Publisher)
Create `index.html` with embedded chart and data table

### Step 6: Deploy (The Courier)
```bash
git add -A
git commit -m "📊 Market update: $(date '+%Y-%m-%d %H:%M %Z')"
git push origin main
```

## Expected Outputs

| File | Description |
|------|-------------|
| `crypto_raw.json` | Raw API response (50 coins) |
| `volatile_movers.json` | Filtered volatile coins |
| `volatility_report.json` | Analysis statistics |
| `daily_brief.txt` | Human-readable summary |
| `generate_chart.py` | Visualization script |
| `market_chart.png` | Bar chart image |
| `index.html` | Web dashboard |

## Error Handling
- If API fails, retry after 60 seconds
- If no volatile coins, create "calm market" report
- If git push fails, report error but don't stop

## Success Criteria
Report the GitHub Pages URL and confirm all 7 output files were created.
