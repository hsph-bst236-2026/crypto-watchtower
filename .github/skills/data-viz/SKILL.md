---
name: data-viz
description: Guide for creating data visualizations with Python Matplotlib. Use this when asked to generate charts, graphs, or visual reports from crypto data.
---

# Data Visualization Skill: Matplotlib Charts

## Overview
This skill covers creating publication-quality visualizations from cryptocurrency market data using Python and Matplotlib.

## Standard Chart: Horizontal Bar Chart

### Complete Template
```python
#!/usr/bin/env python3
"""Generate market movers bar chart from volatile coins data."""
import json
import matplotlib.pyplot as plt
from pathlib import Path

# Configuration
INPUT_FILE = 'volatile_movers.json'
OUTPUT_FILE = 'market_chart.png'
DPI = 300

# Color scheme (accessible, dark-mode friendly)
COLOR_GAIN = '#00ff88'   # Bright green
COLOR_LOSS = '#ff4444'   # Bright red
COLOR_BG = '#1a1a2e'     # Dark background
COLOR_TEXT = '#eeeeee'   # Light text

def load_data(filepath: str) -> list:
    """Load coin data from JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_chart(coins: list, output_path: str) -> None:
    """Create and save horizontal bar chart."""
    if not coins:
        print("No data to visualize")
        return
    
    # Prepare data
    coins_sorted = sorted(coins, key=lambda x: x['price_change_percentage_24h'])
    names = [f"{c['symbol'].upper()}" for c in coins_sorted]
    changes = [c['price_change_percentage_24h'] for c in coins_sorted]
    colors = [COLOR_GAIN if c > 0 else COLOR_LOSS for c in changes]
    
    # Create figure with dark background
    fig, ax = plt.subplots(figsize=(10, max(6, len(names) * 0.4)))
    fig.patch.set_facecolor(COLOR_BG)
    ax.set_facecolor(COLOR_BG)
    
    # Create bars
    bars = ax.barh(names, changes, color=colors, edgecolor='white', linewidth=0.5)
    
    # Add value labels on bars
    for bar, change in zip(bars, changes):
        width = bar.get_width()
        label_x = width + 0.5 if width > 0 else width - 0.5
        ha = 'left' if width > 0 else 'right'
        ax.text(label_x, bar.get_y() + bar.get_height()/2, 
                f'{change:+.1f}%', va='center', ha=ha, 
                color=COLOR_TEXT, fontsize=9)
    
    # Styling
    ax.set_xlabel('24h Price Change (%)', color=COLOR_TEXT, fontsize=12)
    ax.set_title('🔥 Crypto Market Movers', color=COLOR_TEXT, fontsize=16, pad=20)
    ax.tick_params(colors=COLOR_TEXT)
    ax.spines['bottom'].set_color(COLOR_TEXT)
    ax.spines['left'].set_color(COLOR_TEXT)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Add zero line
    ax.axvline(x=0, color=COLOR_TEXT, linewidth=0.5, alpha=0.5)
    
    # Save
    plt.tight_layout()
    fig.savefig(output_path, dpi=DPI, bbox_inches='tight', 
                facecolor=COLOR_BG, edgecolor='none')
    plt.close(fig)
    print(f"✅ Chart saved: {output_path}")

if __name__ == "__main__":
    coins = load_data(INPUT_FILE)
    create_chart(coins, OUTPUT_FILE)
```

## Color Schemes

### Dark Mode (Default)
```python
COLOR_BG = '#1a1a2e'      # Deep blue-black
COLOR_TEXT = '#eeeeee'    # Off-white
COLOR_GAIN = '#00ff88'    # Neon green
COLOR_LOSS = '#ff4444'    # Bright red
COLOR_ACCENT = '#4cc9f0'  # Cyan accent
```

### Light Mode Alternative
```python
COLOR_BG = '#ffffff'
COLOR_TEXT = '#333333'
COLOR_GAIN = '#2e7d32'    # Forest green
COLOR_LOSS = '#c62828'    # Dark red
```

### Colorblind-Friendly
```python
COLOR_GAIN = '#0077bb'    # Blue instead of green
COLOR_LOSS = '#ee7733'    # Orange instead of red
```

## Chart Types Reference

### Pie Chart (Market Cap Distribution)
```python
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(market_caps, labels=names, autopct='%1.1f%%', 
       colors=plt.cm.Set3.colors)
ax.set_title('Market Cap Distribution')
```

### Line Chart (Price History)
```python
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(dates, prices, color=COLOR_ACCENT, linewidth=2)
ax.fill_between(dates, prices, alpha=0.3, color=COLOR_ACCENT)
ax.set_xlabel('Date')
ax.set_ylabel('Price (USD)')
```

### Scatter Plot (Volume vs Change)
```python
fig, ax = plt.subplots(figsize=(10, 8))
scatter = ax.scatter(volumes, changes, c=changes, 
                     cmap='RdYlGn', s=100, alpha=0.7)
plt.colorbar(scatter, label='24h Change %')
```

## Best Practices

| Practice | Why |
|----------|-----|
| Use `fig, ax` pattern | More control than `plt.` functions |
| Always call `plt.close(fig)` | Prevents memory leaks |
| Set `dpi=300` for output | Publication quality |
| Use `bbox_inches='tight'` | No cut-off labels |
| Set `encoding='utf-8'` | Handle emoji/special chars |
| Use `facecolor` in savefig | Preserves background |

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Labels cut off | Add `bbox_inches='tight'` |
| Blurry output | Increase `dpi` (300+) |
| Memory warnings | Call `plt.close()` after each figure |
| Missing fonts | Use system fonts or install `matplotlib` fonts |
| Wrong colors in saved file | Specify `facecolor` in `savefig()` |
