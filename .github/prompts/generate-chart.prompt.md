---
mode: 'agent'
description: 'Generate a matplotlib bar chart from volatile_movers.json showing market movers'
tools: ['editFiles', 'terminalLastCommand']
---

# Generate Market Chart

Create and run a Python script to visualize the volatile coins as a horizontal bar chart.

## Task

1. Create a Python script `generate_chart.py` that:
   - Loads `volatile_movers.json`
   - Creates a horizontal bar chart sorted by price change
   - Uses green (#00ff88) for gains, red (#ff4444) for losses
   - Dark background (#1a1a2e) for consistency with dashboard
   - Saves as `market_chart.png` at 300 DPI

2. Run the script to generate the chart

## Prerequisites
- `volatile_movers.json` must exist (run filter-volatile prompt first)
- Python with matplotlib installed

## Expected Code Structure
```python
import json
import matplotlib.pyplot as plt

# Load data
# Sort by price change
# Create figure with dark background
# Create horizontal bars with conditional coloring
# Add labels, title, styling
# Save and close
```

## Output
- File: `generate_chart.py` (script)
- File: `market_chart.png` (generated chart image)
