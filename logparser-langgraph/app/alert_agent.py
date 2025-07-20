def alert_node(state):
    logs = state.get("logs", [])
    alerts = [log for log in logs if "ERROR" in log]
    return {"alerts": alerts}