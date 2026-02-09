---
name: code-revise
description: Patterns and strategies for fixing code issues identified during review. Use this when asked to fix bugs, refactor code, or apply best practices.
---

# Code Revise Skill: Refactoring & Fixes

## Overview
This skill provides patterns for revising Python code based on review findings, including common fixes, refactoring strategies, and testing approaches.

## Fix Patterns

### 1. Add Error Handling

**Before:**
```python
data = json.load(open('data.json'))
```

**After:**
```python
import sys

try:
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: data.json not found. Run fetch step first.", file=sys.stderr)
    sys.exit(1)
except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON in data.json - {e}", file=sys.stderr)
    sys.exit(1)
```

### 2. Add Type Hints

**Before:**
```python
def process_coins(coins):
    return [c for c in coins if c['price_change_percentage_24h'] > 5]
```

**After:**
```python
from typing import TypedDict

class Coin(TypedDict):
    name: str
    symbol: str
    current_price: float
    price_change_percentage_24h: float

def process_coins(coins: list[Coin]) -> list[Coin]:
    """Filter coins with >5% price change."""
    return [c for c in coins if c['price_change_percentage_24h'] > 5]
```

### 3. Extract Constants

**Before:**
```python
if coin['price_change_percentage_24h'] > 5 or coin['price_change_percentage_24h'] < -5:
    # ...
if coin['price_change_percentage_24h'] < -10:
    print("WARNING!")
```

**After:**
```python
# Configuration
VOLATILITY_THRESHOLD = 5.0  # Percentage for volatile classification
WARNING_THRESHOLD = -10.0   # Percentage for major drop warning

if abs(coin['price_change_percentage_24h']) > VOLATILITY_THRESHOLD:
    # ...
if coin['price_change_percentage_24h'] < WARNING_THRESHOLD:
    print("WARNING!")
```

### 4. Fix Resource Leaks

**Before:**
```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.bar(names, values)
plt.savefig('chart.png')
# Figure never closed - memory leak!
```

**After:**
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(names, values)
fig.savefig('chart.png', dpi=300, bbox_inches='tight')
plt.close(fig)  # Explicitly close to free memory
```

### 5. Handle Empty Data

**Before:**
```python
top_gainer = max(coins, key=lambda x: x['price_change_percentage_24h'])
```

**After:**
```python
if not coins:
    print("No coins to analyze")
    top_gainer = None
else:
    top_gainer = max(coins, key=lambda x: x['price_change_percentage_24h'])
```

### 6. Add Main Guard

**Before:**
```python
# Script runs immediately on import
data = load_data()
process(data)
```

**After:**
```python
def main() -> None:
    """Main entry point."""
    data = load_data()
    process(data)

if __name__ == "__main__":
    main()
```

## Refactoring Strategies

### Extract Function
When code block does one specific thing, extract it:

```python
# Before: Inline logic
colors = []
for c in changes:
    if c > 0:
        colors.append('#00ff88')
    else:
        colors.append('#ff4444')

# After: Extracted function
def get_bar_color(change: float) -> str:
    """Return green for gains, red for losses."""
    return '#00ff88' if change > 0 else '#ff4444'

colors = [get_bar_color(c) for c in changes]
```

### Use Pathlib for Paths
```python
# Before
import os
output_path = os.path.join(os.getcwd(), 'output', 'chart.png')

# After
from pathlib import Path
output_path = Path.cwd() / 'output' / 'chart.png'
output_path.parent.mkdir(exist_ok=True)
```

## Testing Approach

### Quick Validation
```bash
# 1. Syntax check
python -m py_compile script.py && echo "✅ Syntax OK"

# 2. Run with test data
echo '[{"name":"Test","price_change_percentage_24h":10}]' > test.json
python script.py

# 3. Check output exists
ls -la output_file.* && echo "✅ Output created"
```

### Smoke Test Pattern
```python
def test_script():
    """Basic smoke test for the script."""
    import subprocess
    result = subprocess.run(
        ['python', 'script.py'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Script failed: {result.stderr}"
    assert Path('expected_output.json').exists()
```

## Revision Workflow

1. **Read** the review findings
2. **Prioritize** fixes (critical → warning → suggestion)
3. **Apply** each fix pattern
4. **Test** after each change
5. **Document** what was changed
