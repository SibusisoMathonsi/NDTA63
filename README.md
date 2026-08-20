# 🍽️ South African Food Security Analysis & Visualisation

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/) 
[![Data Analysis](https://img.shields.io/badge/Analysis-NumPy%20%7C%20Pandas-green.svg)](https://numpy.org)
[![Database](https://img.shields.io/badge/Database-MySQL-blue.svg)](https://www.mysql.com/)
[![Visualisation](https://img.shields.io/badge/Visualisation-Matplotlib%20%7C%20Seaborn-orange.svg)](https://matplotlib.org)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black.svg)

> **Professional, production-grade data analysis pipeline** combining World Bank datasets to investigate South African food security trends, severity distribution, and population impacts from 2018-2023.

---

## 📊 Project Overview

This comprehensive data analysis project investigates **South African food security** using two complementary World Bank datasets spanning 6 years of trend data and a detailed 2020 snapshot of food security phase distribution. The analysis reveals critical insights into food insecurity prevalence, severity progression, and affected populations.

**Key Finding:** Severe food insecurity prevalence increased **23.19% from 2018 to 2023** (6.9% → 8.5%), with **9.3 million South Africans (16.0%)** classified in crisis-or-worse food insecurity conditions as of October 2020.

---

## 🎯 Project Objectives

- **Establish data provenance** — Track all data sources, transformations, and outputs for auditability
- **Clean and validate data** — Handle missing values, normalize formats, and document data quality
- **Perform rigorous numerical analysis** — Use NumPy arrays to calculate trends, distributions, and key metrics
- **Create stakeholder-ready visualizations** — Develop professional charts that communicate complex findings clearly
- **Implement database integration** — Build a queryable MySQL database with normalized schema and safe operations
- **Enable reproducibility** — Construct a Python pipeline that regenerates all outputs from raw extracts
- **Communicate findings professionally** — Generate comprehensive reports, demos, and documentation for employers and stakeholders

---

## 📈 Key Findings

| Metric | Finding | Impact |
|--------|---------|--------|
| **Prevalence Trend** | 6.9% (2018) → 8.5% (2023) | +23.19% increase over 5 years |
| **Average Prevalence** | 7.95% across 2018-2023 | ~8 in 100 South Africans affected |
| **Crisis+ Population** | 9,335,159 people | 16.0% of classified population (Oct 2020) |
| **Secure Population** | 49,795,278 people | 84.0% in Phase 1-2 (Oct 2020) |
| **Later Period (2021-23)** | 8.43% avg vs 7.47% (2018-20) | 0.97pp worsening in most recent years |
| **Largest YoY Change** | +0.6pp (2018→2019) | Biggest single-year increase |
| **Data Quality** | 6 SVFI years, 12 IPC obs. | 100% completeness (SVFI); 2 missing IPC Phase 5 |

---

## 📚 Datasets: Why These? Where From?

### Dataset 1: Severe Food Insecurity (SVFI) Prevalence
**Source:** World Bank Data360 / World Development Indicators (WDI)  
**Indicator Code:** `WB_WDI_SN_ITK_SVFI_ZS`  
**Measure:** Percentage of population experiencing severe food insecurity  
**Coverage:** 6 annual observations (2018–2023)  
**Geography:** South Africa (ZAF)

**Why Chosen:**
- Provides **long-term trend perspective** spanning 6 consecutive years
- Standardized World Bank methodology ensures international comparability
- Expressed as % of population (relatable to policymakers and public)
- Enables calculation of year-on-year changes and rolling averages

**Data Quality:**
- ✅ No missing values in South Africa series
- ✅ Consistent annual reporting
- ✅ Clear unit definition (%)

---

### Dataset 2: Integrated Food Security Phase Classification (IPC)
**Source:** World Bank Data360 / World Bank Open Data  
**Database:** `IPC_IPC`  
**Snapshot Date:** October 2020  
**Measures:** Persons and percentages by food security phase  
**Coverage:** 12 records (5 phases × 2 metrics)  
**Geography:** South Africa (ZAF)

**Why Chosen:**
- Provides **severity distribution snapshot** — shows *who is in crisis* vs. secure
- IPC is the international standard for food security classification
- Includes both absolute (persons) and relative (%) metrics for stakeholder communication
- October 2020 timing captures critical period during COVID-19 impacts

**Data Quality & Important Notes:**
- ✅ 10 complete phase records (persons and percentages for Phases 1-4)
- ⚠️ Phase 5 (Famine) values marked as missing, not zero
- ✅ Phase 3+ aggregate independently supplied as 9,335,159 persons (16.0%)

**Complementary Analysis:**
- SVFI trend shows *direction of change* (worsening over time)
- IPC phase distribution shows *severity layers* (who's worst affected)
- Together, they answer: "How bad?" (IPC) and "Getting worse?" (SVFI trend)

---

## 🛠️ Technical Architecture

### Tech Stack
| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Data Processing** | Python 3.10+, Pandas | Load, clean, transform CSV data |
| **Numerical Analysis** | NumPy | Array operations, statistics, reshaping |
| **Database** | MySQL 8.0+ | Normalized data storage, queryability, concurrent access |
| **Visualization** | Matplotlib, Seaborn | Publication-ready charts |
| **Spreadsheets** | OpenPyXL, Excel | Business-friendly analysis workbook |
| **Reporting** | Python, Markdown | Reproducible report generation |
| **Version Control** | Git | Auditability, collaboration tracking |

### Data Pipeline Architecture

```
Raw Datasets (CSV)
       ↓
Data Preparation (Cleaning & Validation)
       ↓
    ├─→ Numeric Analysis (NumPy)
    ├─→ Database Integration (MySQL)
    └─→ Python/Excel Analysis
       ↓
    Visualisation (Charts)
       ↓
   Report & Demo
```

---

## 📁 Repository Structure & Deliverables

| Folder | Contents | Audience |
|--------|----------|----------|
| **Raw datasets/** | Preserved source CSV extracts (NEVER modified) | Auditors, Reviewers |
| **Data Preparation/** | Cleaned SA files, stats, quality notes, validation rules | Data Engineers, QA |
| **Numeric Analysis/** | NumPy summaries, phase distributions, YoY changes | Analysts, Researchers |
| **Python or Excel Data Analysis/** | Reusable pipeline, transformed tables, Excel workbook | Developers, Business Users |
| **Database Integration/** | MySQL DB, schema, queries, safe operations evidence | DBAs, Data Architects |
| **Visualisation/** | Presentation-ready PNG charts & dashboard | Stakeholders, Executives |
| **Report & Demo/** | Final report (DOCX/PDF), demo script, checklist | Presenters, Decision-makers |

### Key Deliverables

| Deliverable | File | Format | Use Case |
|------------|------|--------|----------|
| **Reproducible Pipeline** | `food_security_pipeline.py` | Python (57KB) | Regenerate all outputs from raw data |
| **Analysis Workbook** | `food_security_analysis_workbook.xlsx` | Excel | Business-friendly pivot tables & charts |
| **Executive Dashboard** | `food_security_overview_dashboard.png` | PNG | 1-page visual summary of all findings |
| **Trend Chart** | `severe_food_insecurity_trend.png` | PNG | SVFI prevalence 2018-2023 with trend line |
| **Phase Distribution** | `ipc_phase_distribution_*.png` | PNG | IPC phase breakdown (persons & %) |
| **Database** | `food_security_db` (MySQL) | MySQL | Queryable data store with concurrent access |
| **Schema** | `schema.sql` | SQL | Database structure documentation |
| **Queries** | `queries.sql` | SQL | Reusable analytical queries |
| **Final Report** | `NDTA631_Group_Report.pdf/.docx` | PDF/Word | Comprehensive narrative & findings |
| **Demo Script** | `demo_script.txt` | Text | Step-by-step presentation guide |

---

## 👥 Team & Contributions

| Name | Primary Role | Contributions |
|------|--------------|----------------|
| **Sibusiso Agent Mathonsi** | Project Coordinator, Data Integration Lead | Database schema, overall pipeline architecture, project coordination |
| **Kegoikantse Sebetseba** | Data Preparation & Python Analysis | Data cleaning, transformation logic, Python pipeline development |
| **Agcobile Qabo** | Data Preparation & Analysis | Data validation, quality assurance, statistical summaries |
| **Lebogang Malatjie** | Numerical Analysis & Visualization | NumPy calculations, chart design, visual storytelling |
| **Tlotlo Naledi** | Database Integration & Reporting | MySQL implementation, query optimization, documentation |
| **Tlotlanang Naledi** | Reporting & Stakeholder Communication | Final report writing, demo development, stakeholder materials |
| **Thandi Sebokolodi** | Reporting & Stakeholder Communication | Final report writing, demo development, stakeholder materials |

---

## 🚀 How to Run the Analysis

### Prerequisites

```bash
# Python version
python --version
# Required: Python 3.10 or later (tested with 3.14.6)

# Required dependencies (see requirements.txt)
# - numpy ≥ 1.26.0
# - pandas ≥ 2.1.0
# - matplotlib ≥ 3.8.0
# - seaborn ≥ 0.13.0
# - openpyxl ≥ 3.1.0
```

### Installation & Setup

**Windows (PowerShell):**
```powershell
# Clone or download repository
cd path\to\NDTA63

# Create virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

**Linux/macOS (Bash):**
```bash
cd path/to/NDTA63
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Run the Pipeline

```powershell
# Execute the analysis pipeline
python "Python or Excel Data Analysis\food_security_pipeline.py"
```

**Expected Output:**
```
Food security analysis pipeline completed successfully.
```

The pipeline automatically:
1. ✅ Loads raw CSV extracts
2. ✅ Filters to South Africa records
3. ✅ Cleans and validates data
4. ✅ Performs NumPy numerical analysis
5. ✅ Creates MySQL database
6. ✅ Exports database queries
7. ✅ Generates Excel workbook
8. ✅ Creates publication-ready visualizations
9. ✅ Regenerates report pack

### ⚠️ Important Note
Running the pipeline **overwrites generated files** in most folders. Back up any manual edits or presentation annotations before rerunning. Raw CSV files in `Raw datasets/` are never modified.

---

## 📊 Analysis Methodology

### Data Cleaning Approach
1. **Column Normalization** — Convert to lowercase snake_case for consistency
2. **Geographic Filtering** — Extract South Africa (REF_AREA = ZAF)
3. **Type Coercion** — Explicit numeric conversion with error handling
4. **Missing Value Treatment** — Preserve missing values; don't impute as zero
5. **Time Parsing** — Extract year and month from period fields
6. **Label Standardization** — Create readable phase names and descriptions

### Numerical Analysis Approach
- **Array Operations** — NumPy reshaping, aggregation, and statistical functions
- **Time Series Analysis** — Year-on-year changes, rolling averages, trend identification
- **Distribution Analysis** — Phase breakdowns, percentile calculations, proportion analysis
- **Missing Value Handling** — Retain as NaN in arrays, not converted to 0

### Visualization Principles
- **Clarity** — Single clear message per chart
- **Accessibility** — Color-blind friendly palettes, clear legends
- **Interactivity** — Labeled axes, data sources, confidence statements
- **Context** — Comparisons, benchmarks, and trend annotations

---

## 🗄️ Database Structure

**MySQL Schema (4 tables):**

| Table | Rows | Purpose |
|-------|------|---------|
| `ipc_cleaned` | 12 | Raw IPC phase records (persons & %) |
| `ipc_phase_distribution` | 10 | IPC breakdown by phase (excluding missing Phase 5) |
| `svfi_trend` | 6 | Annual SVFI prevalence 2018-2023 |
| `ipc_phase_summary` | 5 | Phase-level totals and proportions |

**Sample Query (Crisis+ Population):**
```sql
SELECT 
    phase_label,
    people,
    percentage
FROM ipc_phase_distribution
WHERE phase IN (3, 4)  -- Crisis or worse
ORDER BY phase;
```

**Result:** 9,335,159 persons (16.0% of classified population)

---

## 📈 Key Insights & Interpretation

### Trend Analysis (SVFI 2018-2023)

| Period | Average | Change | Interpretation |
|--------|---------|--------|-----------------|
| **2018-2020** | 7.47% | Baseline | Gradual increase from 6.9% |
| **2021-2023** | 8.43% | +0.97pp | **Acceleration** — worsening conditions |
| **5-Year Total** | 7.95% | +1.6pp | **23% relative increase** — concerning trend |

**Implication:** Severe food insecurity is worsening over time, suggesting deteriorating economic conditions, labor market pressures, or policy challenges.

---

### Phase Distribution Insight (IPC 2020-10)

```
Phase 1 (Food Secure):        34,481,878 people (58.3%)
Phase 2 (Mildly Insecure):    15,313,400 people (25.9%)
─────────────────────────────────────────────────────
Phase 3 (Crisis):              4,893,827 people (8.3%)
Phase 4 (Emergency):           4,441,332 people (7.5%)
Phase 5 (Famine):             NOT REPORTED
─────────────────────────────────────────────────────
Phase 3+ (Crisis or Worse):    9,335,159 people (16.0%)
```

**Interpretation:**
- ✅ **84%** of classified population achieving basic food security (Phases 1-2)
- ⚠️ **8.3%** in crisis conditions requiring humanitarian assistance
- 🔴 **7.5%** in emergency (livelihood collapse), approaching famine
- ❓ Phase 5 (famine) missing — likely UN IPC data quality constraint for SA

---

## 🔍 Data Quality & Limitations

| Issue | Treatment | Impact |
|-------|-----------|--------|
| **IPC Phase 5 Missing** | Retained as NaN; labeled "Not reported" | Cannot confirm famine prevalence; use Phase 3+ KPI instead |
| **SVFI 2018-2023 Only** | 6-year series (limited history) | Cannot assess pre-2018 baseline or longer-term cycles |
| **IPC Oct 2020 Snapshot** | Single point-in-time; during COVID-19 | May not represent "normal" conditions; useful for severity context |
| **Different Metrics** | SVFI % vs IPC persons+% | Used as complementary views, not directly comparable |

**Recommendation for Stakeholders:** Use SVFI trend to discuss *direction of change* and IPC phase distribution to discuss *current severity*. Avoid implying Phase 5 values without updating from source.

---

## 📋 Verification Checklist

After running the pipeline, confirm these artifacts exist:

- ✅ `Data Preparation/cleaned_*.csv` (3 files)
- ✅ `Data Preparation/data_validation_results.csv`
- ✅ `Numeric Analysis/numerical_summary.csv`
- ✅ `Numeric Analysis/ipc_phase_summary.csv`
- ✅ `Numeric Analysis/severe_food_insecurity_year_on_year_change.csv`
- ✅ `Python or Excel Data Analysis/food_security_pipeline.py` (57KB)
- ✅ `Python or Excel Data Analysis/food_security_analysis_workbook.xlsx`
- ✅ `Database Integration/food_security.db` (28KB)
- ✅ `Database Integration/query_result_*.csv` (3 files)
- ✅ `Visualisation/food_security_overview_dashboard.png`
- ✅ `Visualisation/severe_food_insecurity_trend.png`
- ✅ `Visualisation/ipc_phase_distribution_*.png` (2 files)
- ✅ `Report & Demo/NDTA631_Group_Report.pdf` & `.docx`

---

## 📚 Documentation

| Document | Purpose | Audience |
|----------|---------|----------|
| [DATA_SOURCES_AND_PROVENANCE.md](DATA_SOURCES_AND_PROVENANCE.md) | Complete data lineage, source identifiers, download guidance | Auditors, Data Stewards |
| [SUBMISSION_ASSESSMENT.md](SUBMISSION_ASSESSMENT.md) | Detailed marking rubric & self-assessment | Evaluators, Instructors |
| `*/PROCESS.txt` | Workflow explanation for each folder | Technical Users |
| `Visualisation/chart_explanations.txt` | Interpretation guide for each chart | Stakeholders |
| `Report & Demo/demo_script.txt` | Live presentation walkthrough | Presenters |
| `Report & Demo/final_submission_checklist.txt` | Verification items | Project Managers |

---

## 🎓 Skills Demonstrated

| Skill Category | Evidence |
|---|---|
| **Data Engineering** | ETL pipeline, data validation, quality checks, normalization |
| **Python Development** | OOP design, error handling, comprehensive documentation, 57KB codebase |
| **Data Analysis** | NumPy arrays, reshaping, aggregations, statistical calculations |
| **SQL & Databases** | MySQL schema design, normalized tables, complex queries, safe operations |
| **Visualization** | Matplotlib/Seaborn, professional charts, color theory, accessibility |
| **Documentation** | Clear technical writing, process guides, stakeholder communication |
| **Version Control** | Git commits, collaboration workflow, audit trail |
| **Team Coordination** | Cross-functional teamwork, division of responsibilities, integration |
| **Problem Solving** | Missing data handling, phase interpretation, quality assurance |
| **Communication** | Executive summaries, demo scripts, multiple report formats |

---

## 📞 Contact & Support

For questions about this analysis:
- **Project Lead:** Sibusiso Agent Mathonsi
- **LinkedIn:** [linkedin.com/in/agent-sibusiso-mathonsi-75923a3a0](https://www.linkedin.com/in/agent-sibusiso-mathonsi-75923a3a0)
- **Data Requests:** See [DATA_SOURCES_AND_PROVENANCE.md](DATA_SOURCES_AND_PROVENANCE.md)
- **Technical Issues:** Check `*/PROCESS.txt` files in each folder

---

## 📄 License & Attribution

**Data Source Attribution:**
- World Bank Data360 / World Development Indicators (WB_WDI)
- World Bank Data360 / Integrated Food Security Phase Classification (IPC_IPC)

See [DATA_SOURCES_AND_PROVENANCE.md](DATA_SOURCES_AND_PROVENANCE.md) for complete source citations and download guidance.

---

## Repository structure

| Folder | Contents |
| --- | --- |
| `Raw datasets/` | Preserved source CSV extracts. Do not edit these files. |
| `Data Preparation/` | South Africa cleaned files, descriptive statistics, and data-quality notes. |
| `Numeric Analysis/` | Numerical summaries, phase tables, and year-on-year calculations. |
| `Python or Excel Data Analysis/` | Reusable Python pipeline, transformed tables, and Excel workbook. |
| `Database Integration/` | MySQL database, schema, query script, query exports, and safe-operation evidence. |
| `Visualisation/` | Final labelled PNG charts and chart explanations. |
| `Report & Demo/` | Markdown, DOCX, and PDF report versions plus demo material. |

Each workflow folder includes a `PROCESS.txt` guide describing its role in the pipeline.

## Data provenance

The project uses two locally supplied World Bank Data360 extracts:

- `WB_WDI_SN_ITK_SVFI_ZS.csv` — World Development Indicators, indicator `WB_WDI_SN_ITK_SVFI_ZS`, *Prevalence of severe food insecurity in the population (%)*.
- `IPC_IPC.csv` — Integrated Food Security Phase Classification database, including `IPC_IPC_P3PLUS` and phase-level observations.

Read [DATA_SOURCES_AND_PROVENANCE.md](DATA_SOURCES_AND_PROVENANCE.md) before presenting the results. It records the source identifiers, country filters, data limitations, and the Phase 5 interpretation constraint. The supplied extracts do not include a download URL or retrieval timestamp, so those fields should be added from the source portal before any external publication.

## Reproduce the analysis

### Prerequisites

- Python 3.10 or later (the current project environment was tested with Python 3.14.6).
- Internet access is not required to run the pipeline because the input extracts are stored locally.
- Microsoft Excel or a compatible spreadsheet application is recommended for reviewing the generated workbook.

### Setup

From the repository root in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If script execution is restricted on a managed Windows device, activate the environment using the organisation-approved method, then run the same `pip` commands.

### Run

```powershell
python "Python or Excel Data Analysis\food_security_pipeline.py"
```

The script checks for both raw CSV inputs, filters South Africa records, creates cleaned and numerical outputs, writes the MySQL database and query exports, creates the Excel workbook and visualisations, and regenerates the report/demo pack. A successful run ends with:

```text
Food security analysis pipeline completed successfully.
```

> **Important:** Running the pipeline intentionally replaces generated files in `Data Preparation/`, `Numeric Analysis/`, `Database Integration/`, `Visualisation/`, `Python or Excel Data Analysis/`, and `Report & Demo/`. Preserve any manual edits or presentation annotations before rerunning it. It does not modify the raw source CSV files.

## Verification checklist

After a successful run, confirm that these evidence items are present:

- `Data Preparation/cleaned_severe_food_insecurity_south_africa.csv` and `cleaned_ipc_phase_distribution_south_africa.csv`
- `Numeric Analysis/numerical_summary.csv` and `ipc_phase_summary.csv`
- `Python or Excel Data Analysis/food_security_analysis_workbook.xlsx`
- `Database Integration/food_security.db` plus `query_result_*.csv`
- `Visualisation/food_security_overview_dashboard.png`
- `Report & Demo/NDTA631_Group_Report.pdf`

Open the Excel workbook to validate the analysis tables and embedded charts, and use the generated PNG files as report or slide exports. When discussing results, retain the units exactly as labelled: percentages for severe food insecurity, people/percentage for the IPC snapshot, and percentage points for year-on-year changes.

## Database integration

The pipeline creates `Database Integration/food_security.db` with these analytical tables:

- `ipc_cleaned`
- `ipc_phase_distribution`
- `severe_food_insecurity`
- `ipc_phase_summary`

`schema.sql` documents the analytical fields, and `queries.sql` records the SELECT statements and safe UPDATE/DELETE examples. The safe examples use `WHERE` clauses and a copied demonstration table; they are evidence of safe-query patterns, not a change to the production analytical data. Exported query results provide an auditable bridge between MySQL and the report/visual outputs.

## Technology stack

| Area | Tooling |
| --- | --- |
| Data preparation and analysis | Python, Pandas, NumPy |
| Visualisation | Matplotlib and Seaborn; Excel workbook charts for spreadsheet review |
| Database | MySQL 8.0+ through Python's `mysql-connector-python` package |
| Excel output | OpenPyXL |
| Report generation | Python standard library, Matplotlib PDF backend, and generated DOCX/PDF artifacts |

Exact third-party package versions used in the current project environment are pinned in `requirements.txt`.
