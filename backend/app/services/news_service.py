"""
KunLun — News Service
Scraping, AI analysis (Claude), keyword extraction, factor generation.
"""
import logging
from typing import List
from app.data.models import NewsArticle, NewsFactor

logger = logging.getLogger("kunlun.service.news")


class NewsService:

    async def fetch_latest(self, limit: int = 50) -> List[NewsArticle]:
        """
        Aggregate news from multiple sources:
        - 财联社 (CLS)
        - 新浪财经
        - Reuters / Bloomberg (English)
        Returns raw articles before AI processing.
        """
        raise NotImplementedError

    async def analyze_sentiment(self, articles: List[NewsArticle]) -> List[NewsArticle]:
        """
        Call Claude API to:
        1. Classify sentiment (positive / negative / neutral)
        2. Extract keywords
        3. Identify related tickers
        Returns enriched articles.
        """
        raise NotImplementedError

    async def generate_factors(self, articles: List[NewsArticle]) -> List[NewsFactor]:
        """
        Aggregate keywords across articles, compute frequency and
        average sentiment to produce quantifiable news factors.
        """
        raise NotImplementedError

    async def get_hot_keywords(self, hours: int = 24) -> List[dict]:
        """Return top trending keywords in the last N hours."""
        raise NotImplementedError


news_service = NewsService()
