---
name: data-analysis
description: Guide for filtering and analyzing JSON data using jq and Python. Use this for processing crypto market data and identifying volatile coins.
---

# Data Analysis Skill: jq & Python Processing

## Overview
This skill covers filtering JSON data with `jq` and performing statistical analysis with Python to identify market movers.

## jq Filtering

### Volatility Filter (±5% threshold)
```bash
jq '[.[] | select(.price_change_percentage_24h > 5 or .price_change_percentage_24h < -5)]' crypto_raw.json > volatile_movers.json
```

### With Field Selection (cleaner output)
```bash
jq '[.[] | select(.price_change_percentage_24h > 5 or .price_change_percentage_24h < -5) | {
  name,
  symbol,
  current_price,
  price_change_percentage_24h,
  market_cap
}]' crypto_raw.json > volatile_movers.json
```

### Top Gainers Only
```bash
jq '[.[] | select(.price_change_percentage_24h > 5)] | sort_by(-.price_change_percentage_24h)' crypto_raw.json
```

### Top Losers Only
```bash
jq '[.[] | select(.price_change_percentage_24h < -5)] | sort_by(.price_change_percentage_24h)' crypto_raw.json
```

## jq Syntax Reference

| Expression | Description |
|------------|-------------|
| `.[]` | Iterate over array elements |
| `select(condition)` | Filter by condition |
| `{field1, field2}` | Project specific fields |
| `sort_by(.field)` | Sort ascending |
| `sort_by(-.field)` | Sort descending |
| `[...]` | Collect into array |
| `.field // default` | Default value if null |

## Python Analysis Script

```python
#!/usr/bin/env python3
"""Analyze volatile cryptocurrency movers."""
import json
from datetime import datetime
from statistics import mean, stdev

def load_data(filepath: str) -> list:
    """Load JSON data from file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def analyze_volatility(coins: list) -> dict:
    """Generate volatility statistics."""
    if not coins:
        return {"status": "calm", "message": "No volatile coins found"}
    
    changes = [c['price_change_percentage_24h'] for c in coins]
    gainers = [c for c in coins if c['price_change_percentage_24h'] > 0]
    losers = [c for c in coins if c['price_change_percentage_24h'] < 0]
    
    return {
        "timestamp": datetime.now().isoformat(),
        "total_volatile": len(coins),
        "gainers_count": len(gainers),
        "losers_count": len(losers),
        "avg_change": round(mean(changes), 2),
        "std_dev": round(stdev(changes), 2) if len(changes) > 1 else 0,
        "top_gainer": max(coins, key=lambda x: x['price_change_percentage_24h']),
        "top_loser": min(coins, key=lambda x: x['price_change_percentage_24h']),
        "total_market_cap": sum(c.get('market_cap', 0) for c in coins)
    }

def generate_brief(report: dict) -> str:
    """Generate human-readable summary."""
    if report.get("status") == "calm":
        return "📊 DAILY CRYPTO BRIEF\n\nMarket is calm. No coins moved more than 5% today."
    
    lines = [
        "📊 DAILY CRYPTO BRIEF",
        f"Generated: {report['timestamp'][:19]}",
        "",
        f"🔥 Volatile Coins: {report['total_volatile']}",
        f"   📈 Gainers: {report['gainers_count']}",
        f"   📉 Losers: {report['losers_count']}",
        "",
        f"🏆 TOP GAINER: {report['top_gainer']['name']}",
        f"   +{report['top_gainer']['price_change_percentage_24h']:.1f}%",
        "",
        f"💀 TOP LOSER: {report['top_loser']['name']}",
        f"   {report['top_loser']['price_change_percentage_24h']:.1f}%",
    ]
    
    # Add warning for big drops
    if report['top_loser']['price_change_percentage_24h'] < -10:
        lines.extend([
            "",
            "⚠️  WARNING: MAJOR DROP DETECTED!",
            "    ██████████████████████████",
            "    █  WHALE ALERT: >10% DROP █",
            "    ██████████████████████████",
        ])
    
    return "\n".join(lines)

if __name__ == "__main__":
    coins = load_data("volatile_movers.json")
    report = analyze_volatility(coins)
    
    with open("volatility_report.json", 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, default=str)
    
    brief = generate_brief(report)
    with open("daily_brief.txt", 'w', encoding='utf-8') as f:
        f.write(brief)
    
    print(brief)
```

## Thresholds Reference

| Threshold | Value | Purpose |
|-----------|-------|---------|
| Volatility filter | ±5% | Include in volatile_movers.json |
| Warning trigger | <-10% | Show ASCII whale alert |
| Major gainer | >15% | Highlight in report |
