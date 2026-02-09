Here is the general description of the lecture project, structured to highlight the "Orchestra of Agents" concept.

### **Project Title: The "24/7 Crypto Watchtower"**

**General Description**
In this lecture, we will build a fully automated data pipeline that monitors the cryptocurrency market, identifies significant market movers ("Whales"), visualizes the data, and publishes a live report to a public website.

The core teaching goal is to demonstrate **CLI Orchestration**. Instead of writing code manually in an IDE, we will define five specialized "Agents" (stored as Markdown prompt files). We will then use the Terminal Copilot to chain these agents together, proving that the CLI allows us to act as the *Architect* of a system rather than just a *Typist*.

---

### **The Orchestra: Agents & Skills**

We will build five distinct agents. Each agent possesses a specific "Skill"—a domain of technical expertise that they contribute to the pipeline.

#### **1. The Scout (Data Ingestion Agent)**

* **File:** `skills/fetcher.md`
* **The Task:** Connect to the live internet and retrieve raw data.
* **The Skill:** **`curl` & API Negotiation.**
* *Capability:* It knows how to format HTTP requests, handle API flags (silent, output), and negotiate with the CoinGecko API to get the top 50 coins by market cap in USD.



#### **2. The Editor (Data Engineering Agent)**

* **File:** `skills/filter.md`
* **The Task:** Clean the noisy raw data into high-value insights.
* **The Skill:** **`jq` & JSON Parsing.**
* *Capability:* It fluently speaks the complex `jq` syntax. It filters the raw JSON to find only "volatile" coins (e.g., those that moved >5% in 24 hours) and strips out unnecessary fields, producing a clean `volatile_movers.json`.



#### **3. The Artist (Data Science Agent)**

* **File:** `skills/visualizer.md`
* **The Task:** Turn abstract numbers into a visual story.
* **The Skill:** **Python & Matplotlib.**
* *Capability:* It writes and executes a Python script to generate a `.png` bar chart. It handles the aesthetics: coloring positive gains green and negative losses red, and saving the result as `market_chart.png`.



#### **4. The Publisher (Frontend Agent)**

* **File:** `skills/webmaster.md`
* **The Task:** Package the assets into a human-readable format.
* **The Skill:** **HTML, CSS & Templating.**
* *Capability:* It generates a responsive, dark-mode `index.html` dashboard. It embeds the chart, creates a data table from the JSON, and adds a timestamp, effectively building a static website from scratch.



#### **5. The Courier (DevOps Agent)**

* **File:** `skills/deployer.md`
* **The Task:** Deliver the final product to the world.
* **The Skill:** **Git & CI/CD.**
* *Capability:* It manages version control. It stages the new files, commits them with a dynamic date message, and pushes the changes to a public branch (e.g., GitHub Pages), making the site live instantly.



---

### **The Final Deliverable**

By the end of the lecture, the students will see a **Live Web Dashboard** (hosted on GitHub Pages or opened locally) containing:

1. **A "Breaking News" Headline** with the exact time of the lecture.
2. **A Color-Coded Bar Chart** showing the biggest winners and losers of the last 24 hours.
3. **A Data Table** listing the specific prices of the volatile coins.

**The "Magic" Moment:**
The students will realize that this entire full-stack application (Backend -> Data -> Viz -> Frontend -> DevOps) was built by running 5 terminal commands, orchestrated by them, without writing a single line of manual code.