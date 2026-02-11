import json
import os
from datetime import datetime
from typing import Dict, List, Optional
import config

class Database:
    """Oddiy JSON-based database"""
    
    def __init__(self, db_file: str = None):
        self.db_file = db_file or config.DATABASE_FILE
        self.data = self._load_data()
    
    def _load_data(self) -> dict:
        """Ma'lumotlarni yuklash"""
        if os.path.exists(self.db_file):
            try:
                with open(self.db_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {"users": {}, "analyses": []}
        return {"users": {}, "analyses": []}
    
    def _save_data(self):
        """Ma'lumotlarni saqlash"""
        with open(self.db_file, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)
    
    def save_analysis(self, user_id: int, username: str, schedule_text: str, 
                     analysis_result: str, score: float = None):
        """Tahlilni saqlash"""
        
        analysis = {
            "user_id": user_id,
            "username": username,
            "schedule": schedule_text,
            "analysis": analysis_result,
            "score": score,
            "timestamp": datetime.now().isoformat(),
            "date": datetime.now().strftime("%Y-%m-%d")
        }
        
        self.data["analyses"].append(analysis)
        
        # Foydalanuvchi statistikasini yangilash
        if str(user_id) not in self.data["users"]:
            self.data["users"][str(user_id)] = {
                "username": username,
                "total_analyses": 0,
                "first_analysis": datetime.now().isoformat(),
                "badges": []
            }
        
        self.data["users"][str(user_id)]["total_analyses"] += 1
        self.data["users"][str(user_id)]["last_analysis"] = datetime.now().isoformat()
        
        # Badge berish
        self._check_badges(user_id)
        
        self._save_data()
    
    def _check_badges(self, user_id: int):
        """Badge'larni tekshirish va berish"""
        user_data = self.data["users"][str(user_id)]
        total = user_data["total_analyses"]
        badges = user_data.get("badges", [])
        
        # Badge'lar config dan
        for required_count, badge_name in config.BADGES.items():
            if total >= required_count and badge_name not in badges:
                badges.append(badge_name)
        
        user_data["badges"] = badges
    
    def get_user_stats(self, user_id: int) -> Optional[Dict]:
        """Foydalanuvchi statistikasi"""
        return self.data["users"].get(str(user_id))
    
    def get_user_analyses(self, user_id: int, limit: int = 10) -> List[Dict]:
        """Foydalanuvchining oxirgi tahlillari"""
        user_analyses = [
            a for a in self.data["analyses"] 
            if a["user_id"] == user_id
        ]
        return sorted(user_analyses, key=lambda x: x["timestamp"], reverse=True)[:limit]
    
    def get_week_stats(self, user_id: int) -> Dict:
        """Haftalik statistika"""
        from datetime import timedelta
        
        week_ago = datetime.now() - timedelta(days=7)
        week_analyses = [
            a for a in self.data["analyses"]
            if a["user_id"] == user_id and 
            datetime.fromisoformat(a["timestamp"]) > week_ago
        ]
        
        return {
            "total": len(week_analyses),
            "analyses": week_analyses
        }
    
    def get_leaderboard(self, limit: int = 10) -> List[Dict]:
        """Reyting jadvali"""
        users = []
        for user_id, user_data in self.data["users"].items():
            users.append({
                "user_id": user_id,
                "username": user_data.get("username", "Unknown"),
                "total": user_data["total_analyses"],
                "badges": user_data.get("badges", [])
            })
        
        return sorted(users, key=lambda x: x["total"], reverse=True)[:limit]
