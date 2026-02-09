#!/usr/bin/env python3
"""Analyze volatile cryptocurrency movers and generate reports."""
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
    
    changes = [c['price_change_percentage_24h'] for c in coins if c.get('price_change_percentage_24h') is not None]
    
    if not changes:
        return {"status": "calm", "message": "No valid price changes found"}
    
    gainers = [c for c in coins if c.get('price_change_percentage_24h', 0) and c['price_change_percentage_24h'] > 0]
    losers = [c for c in coins if c.get('price_change_percentage_24h', 0) and c['price_change_percentage_24h'] < 0]
    
    # Find top gainer and loser safely
    valid_coins = [c for c in coins if c.get('price_change_percentage_24h') is not None]
    top_gainer = max(valid_coins, key=lambda x: x['price_change_percentage_24h']) if valid_coins else None
    top_loser = min(valid_coins, key=lambda x: x['price_change_percentage_24h']) if valid_coins else None
    
    return {
        "timestamp": datetime.now().isoformat(),
        "total_volatile": len(coins),
        "gainers_count": len(gainers),
        "losers_count": len(losers),
        "avg_change": round(mean(changes), 2) if changes else 0,
        "std_dev": round(stdev(changes), 2) if len(changes) > 1 else 0,
        "top_gainer": top_gainer,
        "top_loser": top_loser,
        "total_market_cap": sum(c.get('market_cap', 0) or 0 for c in coins)
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
    ]
    
    if report.get('top_gainer'):
        lines.extend([
            f"🏆 TOP GAINER: {report['top_gainer']['name']}",
            f"   +{report['top_gainer']['price_change_percentage_24h']:.1f}%",
            "",
        ])
    
    if report.get('top_loser'):
        lines.extend([
            f"💀 TOP LOSER: {report['top_loser']['name']}",
            f"   {report['top_loser']['price_change_percentage_24h']:.1f}%",
        ])
        
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
    print("\n✅ Step 3: Analysis complete!")
