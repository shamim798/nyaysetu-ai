# NyaySetu AI (ন্যায়সেতু ৩৬০) ⚖️🇧🇩

> **Democratizing Justice through AI-Native Procedural Guidance & Immersive 3D Courtroom Simulation**  
> *Official Submission for the International AI Builders Congress 2026 — Track: JusticeSphere AI (Challenge: Legal Copilot)*

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-green.svg)](https://www.python.org/)
[![FastAPI / Streamlit](https://img.shields.io/badge/Stack-FastAPI%20%7C%20Streamlit-orange.svg)]()
[![Gemini 1.5](https://img.shields.io/badge/AI-Gemini%201.5%20Pro%20%26%20Flash-blueviolet.svg)](https://deepmind.google/technologies/gemini/)

---

## 🌟 Executive Summary
Over **4 million cases** are currently pending in Bangladeshi courts. Millions of citizens refrain from seeking formal legal recourse out of intimidation, procedural obscurity, and extortion by unauthorized middlemen at police stations. On the other hand, thousands of law students graduate every year without practical, adversarial trial experience.

**NyaySetu AI (ন্যায়সেতু ৩৬০)** is an end-to-end, AI-native legal ecosystem engineered to solve this dual crisis:
1. **For Citizens & Victims (B2C):** A voice-first multimodal assistant that translates natural language narratives into legally cited, print-ready police GD (General Diary) and FIR petitions, complete with evidence viability scoring, digital lawyer co-signing, and bKash/Nagad micro-payments.
2. **For Law Students & Practitioners (EdTech & SaaS):** A browser-accessible 3D virtual courtroom (WebXR/Spatial AI) powered by multi-agent adversarial sparring (AI Judge, Hostile Witness, Opposing Counsel), alongside autonomous cross-border contract redlining for global trade.

---

## 🏛️ System Architecture

```
                       ┌────────────────────────────────────────────────────────┐
                       │          NyaySetu Multimodal Ingestion Gateway         │
                       │     (Bangla Voice STT, Plain Text, Scanned Evidence)   │
                       └───────────────────────────┬────────────────────────────┘
                                                   │
                  ┌────────────────────────────────┴────────────────────────────────┐
                  ▼                                                                 ▼
   ┌───────────────────────────────┐                                 ┌───────────────────────────────┐
   │    Citizen Procedural Hub     │                                 │     Immersive Virtual Court   │
   ├───────────────────────────────┤                                 ├───────────────────────────────┤
   │ • Regional Dialect Parser     │                                 │ • 3D WebXR Courtroom Simulation│
   │ • Penal Code / CrPC Matcher   │                                 │ • Multi-Agent Moot Trial      │
   │ • 1-Click GD & FIR Generator  │                                 │   - AI Judge (Procedural Rule)│
   │ • Evidence Strength Scorer    │                                 │   - Hostile Witness Agent     │
   │ • Lawyer Co-Sign & Seal       │                                 │   - Opposing Counsel          │
   └──────────────┬────────────────┘                                 └───────────────┬───────────────┘
                  │                                                                  │
                  └────────────────────────────────┬─────────────────────────────────┘
                                                   ▼
                       ┌────────────────────────────────────────────────────────┐
                       │          Bangla Legal Graph-RAG Ontology               │
                       │ • Penal Code 1860       • CrPC 1898       • CPC 1908   │
                       │ • Supreme Court Rulings • Cyber Security Act           │
                       └───────────────────────────┬────────────────────────────┘
                                                   ▼
                       ┌────────────────────────────────────────────────────────┐
                       │   Local & Global Monetization (From Idea to Unicorn)   │
                       │ • bKash/Nagad ৳50 Micro-Checkout (GD/FIR Downloads)    │
                       │ • 10-15% Marketplace Commission on Verified Advocates │
                       │ • B2B University SaaS Licensing for 3D Moot Courts     │
                       └────────────────────────────────────────────────────────┘
```

---

## 🚀 Key Features

### 1. 📢 Voice-First Police GD & FIR Generator
- Accepts incident narratives in standard Bangla, regional dialects (Chittagonian, Sylheti, Noakhali), or plain English.
- Maps facts to statutory offenses under the **Penal Code 1860**, **CrPC 1898**, or the **Cyber Security Act**.
- Automatically formats and outputs official, ready-to-print petitions addressed to the Officer-in-Charge (OC) of the relevant police station.

### 2. 🛡️ Zero-Knowledge Evidence Strength Auditor
- Analyzes uploaded screenshots, receipts, voice notes, or documents.
- Evaluates admissibility under the **Evidence Act 1872** and generates a strength percentage score with itemized checklists of missing corroborating evidence.
- Client-side end-to-end encryption ensures user confidentiality.

### 3. 👨‍⚖️ 3D Virtual Moot Courtroom (WebXR / Spatial AI)
- Browser-based 3D courtroom where students conduct examination-in-chief and cross-examinations.
- AI Judge rules on real-time objections (`Sustained` vs. `Overruled`) based on evidence and procedural law.

### 4. 🌐 Cross-Border Contract & Freelance Protector
- Automatically scans international freelance contracts, NDAs, and service agreements.
- Generates risk heatmaps for unfair liability clauses, intellectual property transfers, and payment arbitration terms.
- 1-click switching between Bangladesh law, UK Common Law, and US statutes.

### 5. 💳 Hyper-Localized Monetization Engine
- Instant **bKash & Nagad** checkout for ৳50–৳100 petition downloads.
- Optional ৳150 add-on for digital co-signing and verification by registered Supreme Court / Bar Council lawyers.

---

## 🛠️ Technology Stack

| Layer | Technologies |
| :--- | :--- |
| **Foundation Models** | Google Gemini 1.5 Pro, Gemini 1.5 Flash, Whisper STT/TTS |
| **Knowledge Engine** | Custom Graph-RAG over Bangladesh Statutory Code & Case Law Reports |
| **Backend & Orchestration** | Python 3.11, FastAPI, LangChain, LlamaIndex, ChromaDB / pgvector |
| **Frontend & 3D WebXR** | Streamlit (Prototype), Next.js 14, Three.js / WebXR, Tailwind CSS |
| **Cloud & Security** | Supabase (PostgreSQL, Storage, Realtime Auth), Vercel |
| **Payments** | bKash Checkout API, Nagad Gateway |

---

## 📦 Quick Start & Prototype Run

### 1. Clone the repository
```bash
git clone https://github.com/shamim798/nyaysetu-ai.git
cd nyaysetu-ai
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the interactive prototype
```bash
streamlit run app.py
```

---

## 👥 Team Dododeck
- **Md Shamim Ali** — *Team Lead & AI/Full-Stack Architect* (Multimedia and Creative Technology, Daffodil International University)

---

## 📜 License
This project is licensed under the [MIT License](LICENSE).
