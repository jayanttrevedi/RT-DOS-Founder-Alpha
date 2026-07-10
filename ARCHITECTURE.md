# RT-DOS Founder Alpha Architecture

## Overview

RT-DOS Founder Alpha is a layered trading intelligence platform designed around modular engines, a presentation layer, and a Streamlit-based workspace interface. The architecture separates data acquisition, analysis, decision generation, and user-interface rendering so each component can evolve independently.

---

## Folder Structure

```text
RT-DOS-Founder-Alpha/
├── app.py                 # Streamlit application entry point
├── main.py                # Console-oriented entry point
├── README.md              # Project overview
├── ROADMAP.md             # Product planning document
├── CHANGELOG.md           # Release and milestone history
├── ARCHITECTURE.md        # This file
├── DEVELOPMENT_GUIDELINES.md
├── config/                # Configuration values and app settings
├── data/                  # Local data and watchlist assets
├── docs/                  # Architecture and product documentation
├── engines/               # Core intelligence engines
├── indicators/            # Pure mathematical indicator calculations
├── reports/               # Reporting and output presentation
├── ui/                    # Streamlit UI components and workspaces
└── utils/                 # Shared utility support (if extended)
```

---

## Engine Hierarchy

### 1. Data Layer
- MarketDataEngine
- DataProvider

### 2. Validation Layer
- ValidationEngine

### 3. Consistency Layer
- ConsistencyEngine

### 4. Analysis Layer
- TechnicalEngine
- MomentumEngine
- ATREngine
- VolumeEngine
- RelativeStrengthEngine
- ScoringEngine
- CompositeEngine
- MarketRegimeEngine
- InstitutionalConfidenceEngine
- ProbabilityEngine
- MarketSentinelEngine

### 5. Decision Layer
- DecisionEngine
- ExplainabilityEngine

### 6. Reporting Layer
- ReportEngine

### Design Rule
Each engine should focus on a single responsibility and expose a stable, predictable interface.

---

## UI Hierarchy

### Shell Layer
- Navigation
- WorkspaceRouter
- Theme

### Workspace Layer
- Dashboard
- MarketHeader
- ExecutiveRibbon
- SummaryPanel
- OpportunityRadar
- RankingPanel
- DailyBrief
- ExecutiveAlerts

### Presentation Layer
- Market health widgets
- Market breadth widgets
- KPI strip and status display
- Executive commentary and alert display

### Rule
UI components must remain presentation-only and should not calculate intelligence.

---

## Data Flow

```text
Market Data
  -> Validation
  -> Consistency Check
  -> Technical Analysis
  -> Composite Scoring
  -> Market Regime / Confidence / Probability
  -> Decision Generation
  -> Presentation Preparation
  -> Streamlit Dashboard
```

### Runtime Flow
1. Application startup loads configuration and market data.
2. Validation ensures the data is usable.
3. The intelligence pipeline runs the analytical engines.
4. Decision engines convert analysis into recommendations.
5. The presentation engine formats outputs for UI consumption.
6. Dashboard and workspace components render the final view.

---

## Design Principles

- Modularity: each subsystem has one clear purpose.
- Separation of concerns: engines do analysis; UI components display results.
- Explainability: the system should provide transparent reasoning paths.
- Extensibility: new engines and UI modules can be added without rewriting the pipeline.
- Stability: default-safe behavior should be available even when live integrations are incomplete.

---

## Dependency Rules

- Engines may depend on other engines only when the dependency expresses a true workflow relationship.
- UI components should not implement business logic.
- Indicators should remain mathematical and stateless.
- Presentation modules should depend on engine output structures rather than hidden state.
- New modules should be introduced through clearly defined interfaces.

---

## Future Extension Points

### Planned Engine Extensions
- Live market-data providers
- Fundamental analysis engine
- Sentiment engine
- News/event ingestion framework
- Portfolio intelligence engine
- Risk management engine
- Broker integration layer

### Planned UI Extensions
- Portfolio workspace
- Scanner workspace
- Risk workspace
- Options workspace
- AI assistant view

### Architectural Goal
The existing architecture is intentionally open-ended so new capabilities can be added without disrupting the core decision pipeline.
