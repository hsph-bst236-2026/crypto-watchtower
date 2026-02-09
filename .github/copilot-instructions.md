---
applyTo: "**"
---
# Crypto Watchtower - AI Agent Pipeline Instructions

## Project Architecture

This is the **"24/7 Crypto Watchtower"** — an automated data pipeline demonstrating CLI Orchestration with AI Agents. The architecture follows a three-tier pattern:

- **Agents** (`.github/agent/`): Orchestrators with tools and decision-making capability
- **Skills** (`.github/skills/`): Domain knowledge modules providing how-to documentation
- **Prompts** (`.github/prompts/`): Quick-trigger task executors for one-click actions

### Data Flow
```
CoinGecko API → crypto_raw.json → volatile_movers.json → market_chart.png → index.html → GitHub Pages
   (fetch)         (filter)           (analyze)            (visualize)        (deploy)
```

---

## Agents (`.github/agent/`)

Agents orchestrate multi-step workflows and have access to tools.

| Agent | File | Purpose |
|-------|------|---------|
| Data Pipeline | `data-pipeline.agent.md` | Fetch, filter, analyze crypto data |
| Code Quality | `code-quality.agent.md` | Review and revise generated code |
| Publisher | `publisher.agent.md` | Visualize, build dashboard, deploy |

### Agent Capabilities
- Use `terminalLastCommand` to run shell commands
- Use `editFiles` to create/modify code
- Use `codebase` to read existing files

---

## Skills (`.github/skills/`)

Skills provide domain expertise as reference documentation.

| Skill | Folder | Expertise |
|-------|--------|-----------|
| Data Fetch | `data-fetch/` | CoinGecko API, `curl` commands |
| Data Analysis | `data-analysis/` | `jq` filtering, Python pandas |
| Code Review | `code-review/` | Quality checklist, anti-patterns |
| Code Revise | `code-revise/` | Refactoring patterns, fixes |
| Data Viz | `data-viz/` | Matplotlib charts, styling |
| GitHub Pages | `github-pages/` | HTML templates, Git deployment |

---

## Prompts (`.github/prompts/`)

Prompts enable one-click task execution.

| Prompt | File | Action |
|--------|------|--------|
| Fetch Crypto | `fetch-crypto.prompt.md` | Get top 50 coins from API |
| Filter Volatile | `filter-volatile.prompt.md` | Find >5% movers with `jq` |
| Generate Chart | `generate-chart.prompt.md` | Create matplotlib bar chart |
| Build Dashboard | `build-dashboard.prompt.md` | Generate dark-mode HTML |
| Deploy Pages | `deploy-pages.prompt.md` | Git commit and push |
| Run Pipeline | `run-pipeline.prompt.md` | Execute full pipeline end-to-end |

---

## Key Implementation Details

### External API
- **CoinGecko API**: `https://api.coingecko.com/api/v3/coins/markets`
- Required params: `vs_currency=usd`, `order=market_cap_desc`, `per_page=50`
- Output format: JSON array with `name`, `current_price`, `price_change_percentage_24h`

### Thresholds
- **Volatility filter**: `|price_change_percentage_24h| > 5%`
- **Warning trigger**: Any coin drops more than `10%` (triggers ASCII whale alert)

### Output Files
| File | Format | Purpose |
|------|--------|---------|
| `crypto_raw.json` | Raw JSON | Full API response (50 coins) |
| `volatile_movers.json` | Filtered JSON | Coins meeting volatility threshold |
| `volatility_report.json` | JSON | Analysis statistics |
| `daily_brief.txt` | Plain text | Human-readable summary |
| `market_chart.png` | PNG | Bar chart visualization |
| `index.html` | HTML | Web dashboard |

---

## Conventions

### Adding New Agents
1. Create `<name>.agent.md` in `.github/agent/`
2. Include YAML frontmatter with `name`, `description`, `tools`
3. Document workflow steps in markdown body

### Adding New Skills
1. Create folder in `.github/skills/<name>/`
2. Add `SKILL.md` with `name` and `description` frontmatter
3. Include comprehensive how-to documentation

### Adding New Prompts
1. Create `<action>.prompt.md` in `.github/prompts/`
2. Include frontmatter with `mode: 'agent'`, `description`, `tools`
3. Write specific task instructions with validation steps

### Python Scripts
- Use snake_case for filenames (e.g., `generate_chart.py`)
- Always specify `encoding='utf-8'` for file I/O
- Use context managers (`with` statements) for resources
- Include type hints and docstrings
