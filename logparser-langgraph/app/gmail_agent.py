from langgraph.graph import StateGraph, Message
from gmail_parser import fetch_emails  # your helper
def gmail_node(state): 
    emails = fetch_emails(state.get("email_query"))
    return {"emails": emails}

graph = StateGraph()
graph.add_node("fetch_gmail", gmail_node)