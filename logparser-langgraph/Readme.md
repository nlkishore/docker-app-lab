To ingest external logs dynamically during container runtime:

log-analyzer/
├── app/
│   ├── graph.py              # LangGraph workflow
│   ├── gmail_agent.py        # Gmail API email parsing
│   ├── alert_agent.py        # Trigger alerts from logs/emails
│   ├── dashboard.py          # Streamlit front-end
│   └── utils.py              # Reusable parsing helpers
├── .env
├── Dockerfile
├── docker-compose.yml
└── requirements.txt