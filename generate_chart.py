#!/usr/bin/env python3
"""Generate market movers bar chart from volatile coins data."""
import json
import matplotlib.pyplot as plt

# Configuration
INPUT_FILE = 'volatile_movers.json'
OUTPUT_FILE = 'market_chart.png'
DPI = 300

# Color scheme (dark-mode friendly)
COLOR_GAIN = '#00ff88'
COLOR_LOSS = '#ff4444'
COLOR_BG = '#1a1a2e'
COLOR_TEXT = '#eeeeee'


def load_data(filepath: str) -> list:
    """Load coin data from JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def create_chart(coins: list, output_path: str) -> None:
    """Create and save horizontal bar chart."""
    if not coins:
        print("No data to visualize")
        return
    
    # Filter coins with valid price changes
    valid_coins = [c for c in coins if c.get('price_change_percentage_24h') is not None]
    
    if not valid_coins:
        print("No valid data to visualize")
        return
    
    # Prepare data
    coins_sorted = sorted(valid_coins, key=lambda x: x['price_change_percentage_24h'])
    names = [f"{c['symbol'].upper()}" for c in coins_sorted]
    changes = [c['price_change_percentage_24h'] for c in coins_sorted]
    colors = [COLOR_GAIN if c > 0 else COLOR_LOSS for c in changes]
    
    # Create figure with dark background
    fig, ax = plt.subplots(figsize=(10, max(6, len(names) * 0.6)))
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
                color=COLOR_TEXT, fontsize=11, fontweight='bold')
    
    # Styling
    ax.set_xlabel('24h Price Change (%)', color=COLOR_TEXT, fontsize=12)
    ax.set_title('🔥 Crypto Market Movers', color=COLOR_TEXT, fontsize=16, pad=20)
    ax.tick_params(colors=COLOR_TEXT, labelsize=11)
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
    print(f"✅ Step 4: Chart saved: {output_path}")


if __name__ == "__main__":
    coins = load_data(INPUT_FILE)
    create_chart(coins, OUTPUT_FILE)
