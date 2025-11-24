# database.py - Supabase Database Integration
import os
from supabase import create_client, Client
from typing import Optional, List, Dict, Any
from datetime import datetime, timedelta
import pandas as pd
import streamlit as st

class SupabaseDB:
    """Supabase database connection and operations"""
    
    def __init__(self):
        # Try to get credentials from Streamlit secrets first, then environment
        try:
            self.url = st.secrets.get("SUPABASE_URL")
            self.key = st.secrets.get("SUPABASE_ANON_KEY")
            self.service_key = st.secrets.get("SUPABASE_SERVICE_KEY")
        except:
            self.url = os.getenv("SUPABASE_URL")
            self.key = os.getenv("SUPABASE_ANON_KEY")
            self.service_key = os.getenv("SUPABASE_SERVICE_KEY")
        
        if not self.url or not self.key:
            raise ValueError("Missing Supabase credentials")
        
        self.client: Client = create_client(self.url, self.key)
    
    def sign_in(self, email: str, password: str) -> Dict[str, Any]:
        """Sign in user"""
        try:
            response = self.client.auth.sign_in_with_password({
                "email": email,
                "password": password
            })
            return {"success": True, "user": response.user, "session": response.session}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_dashboard_metrics(self, user_id: Optional[str] = None) -> Dict:
        """Get dashboard metrics"""
        # Add your implementation here
        return {
            "total_tasks": 0,
            "pending_tasks": 0,
            "my_tasks": 0,
            "completed_tasks": 0
        }

# Global instance
try:
    db = SupabaseDB()
except Exception as e:
    print(f"Database initialization failed: {e}")
    db = None
