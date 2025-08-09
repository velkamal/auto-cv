from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, EmailStr


class Experience(BaseModel):
    """Professional experience entry."""

    company: str
    role: str
    start_date: str
    end_date: Optional[str] = None
    description: Optional[str] = None


class CVRequest(BaseModel):
    """Payload for CV generation."""

    name: str
    email: EmailStr
    phone: Optional[str] = None
    summary: Optional[str] = None
    skills: List[str] = []
    experience: List[Experience] = []
