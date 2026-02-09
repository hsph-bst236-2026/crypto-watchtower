---
mode: 'agent'
description: 'Generate a dark-mode HTML dashboard with embedded chart and data table'
tools: ['editFiles']
---

# Build Dashboard

Create a responsive dark-mode HTML dashboard that displays the crypto market data.

## Task

Create `index.html` with:

### Structure
1. **Header**: Title "🔥 Crypto Watchtower" with timestamp
2. **Chart Section**: Embedded `market_chart.png`
3. **Data Table**: Dynamic table populated from `volatile_movers.json`
4. **Footer**: Attribution and data source

### Styling Requirements
- Dark background: `#1a1a2e`
- Light text: `#eeeeee`
- Accent color: `#4cc9f0`
- Gains: `#00ff88` (green)
- Losses: `#ff4444` (red)
- Responsive (works on mobile)

### JavaScript
- Fetch `volatile_movers.json` and populate table
- Format prices with locale string
- Color-code change percentages
- Show current timestamp

## Prerequisites
- `market_chart.png` must exist (run generate-chart prompt first)
- `volatile_movers.json` must exist

## Output
- File: `index.html` (complete dashboard)
