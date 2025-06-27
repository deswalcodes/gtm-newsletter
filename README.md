# 🗞️ Weekly AI Transcription Digest

**GTM Engineer Intern: 48-Hour Automated Newsletter Challenge**

Welcome to the **Weekly AI Transcription Digest**, a production-grade, scalable, and fully automated newsletter platform focused on *Speech-to-Text & AI Transcription*. This project was built in 48 hours to showcase a professional-grade GTM (Go-To-Market) automation approach with zero manual intervention.

---

## 📌 Project Overview

- **Focus Area**: Speech-to-Text & AI Transcription  
- **Automation**: 95% automated end-to-end newsletter system  
- **Data Sources**: RSS feeds, Google News, Product Hunt, Arxiv, Playwright scraping  
- **LLM**: GPT-powered summarization and curation  
- **Distribution**: Mailchimp campaigns  
- **Workflow Orchestration**: n8n for scheduling and error notifications  
- **Database**: Neon (PostgreSQL) for storing editions  
- **Analytics**: Mailchimp dashboard for open/click rates

---

## 🚀 Features

✅ Fully automated multi-source content collection  
✅ Summarization and story selection using GPT  
✅ Markdown-to-HTML pipeline for professional newsletter output  
✅ Mailchimp API for campaign delivery to subscribers  
✅ Scheduled publishing via n8n cron triggers  
✅ Automated error monitoring and alerting via n8n email node  
✅ Live subscription page for user sign-ups  
✅ Scalable for 1000+ subscribers  
✅ Modular, documented Python codebase

---

## 🏗️ Architecture

```mermaid
flowchart TD
  A[Data Ingestion<br>(RSS, Scraping)] --> B[GPT Summarization]
  B --> C[Markdown Generator]
  C --> D[HTML Formatter]
  D --> E[Mailchimp Campaign API]
  B --> F[Neon DB Save]
  E --> G[Subscribers]
  H[n8n Automation] --> A
  H --> E
  H --> I[Error Notifications]
```
