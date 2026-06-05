from __future__ import annotations

from typing import ClassVar

from pydantic import BaseModel, ConfigDict, Field

class SchemaBaseModel(BaseModel):
    model_config: ClassVar[ConfigDict]

class PersonalInfo(SchemaBaseModel):
    name: str
    email: str
    phone: str | None
    website: str | None
    github: str | None
    linkedin: str | None
    location: str | None

class Education(SchemaBaseModel):
    id: str
    institution: str
    degree: str
    area: str
    start: str
    end: str
    location: str
    advisor: str | None
    details: str | list[str] | None
    formatted: dict[str, dict[str, str]] | None
    notes: str | None

class Experience(SchemaBaseModel):
    id: str
    organization: str
    role: str
    start: str
    end: str
    location: str
    summary: str | None
    bullets: list[str]
    formatted: dict[str, dict[str, str]] | None
    notes: str | None

class Project(SchemaBaseModel):
    id: str
    name: str
    url: str | None
    summary: str | None
    bullets: list[str]
    technologies: list[str]
    formatted: dict[str, dict[str, str]] | None
    notes: str | None

class Honor(SchemaBaseModel):
    id: str
    title: str
    issuer: str | None
    location: str | None
    date: str | None
    summary: str | None
    notes: str | None

class Service(SchemaBaseModel):
    id: str
    role: str
    organization: str
    location: str | None
    date: str | None
    notes: str | None

class Skill(SchemaBaseModel):
    id: str
    category: str
    items: list[str]
    formatted: dict[str, dict[str, str]] | None
    notes: str | None

class Grant(SchemaBaseModel):
    id: str
    title: str
    funder: str
    role: str
    amount: str | None
    start: str | None
    end: str | None
    details: list[str]
    notes: str | None

class Affiliation(SchemaBaseModel):
    id: str
    organization: str
    role: str | None
    date: str | None
    notes: str | None

class Summary(SchemaBaseModel):
    text: str

class PublicationRef(SchemaBaseModel):
    cite_key: str

class PresentationRef(SchemaBaseModel):
    cite_key: str

class ProfessionalData(SchemaBaseModel):
    schema_version: str
    personal_info: PersonalInfo
    education: list[Education]
    research_experience: list[Experience]
    work_experience: list[Experience]
    skills: list[Skill]
    projects: list[Project]
    honors: list[Honor]
    service_leadership: list[Service]
    teaching_experience: list[Experience]
    grants: list[Grant]
    extracurricular: list[Experience]
    affiliations: list[Affiliation]
    wetlab_skills: list[Skill]
    summary: Summary | None
    publications: list[PublicationRef]
    presentations: list[PresentationRef]
