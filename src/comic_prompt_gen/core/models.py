"""Data models for comic prompt generation."""
from typing import Dict, List, Optional, Any
from datetime import datetime
from pydantic import BaseModel, Field


class Panel(BaseModel):
    """Represents a single panel in a comic."""
    
    purpose: str = Field(..., description="The narrative purpose of this panel")
    desc: str = Field(..., description="Visual description of the panel")
    comp: str = Field(..., description="Composition/angle of the panel")
    text: Optional[str] = Field("", description="Text content in the panel")
    placement: str = Field("No text", description="Text placement in the panel")
    sfx: Optional[str] = Field("", description="Sound effects in the panel")
    ref: Optional[str] = Field("", description="Specific references for the panel")
    transition: Optional[str] = Field("", description="Transition from previous panel")


class StyleProfile(BaseModel):
    """Represents the visual style for the comic."""
    
    style_name: str = Field(..., description="Name of the base style")
    char_style: str = Field(..., description="Character style description")
    char_recurring: Optional[str] = Field("", description="Recurring character note")
    char_expressions: str = Field(..., description="Key expressions/emotions")
    line_weight: str = Field(..., description="Line weight style")
    line_style: str = Field(..., description="Line style")
    line_color: str = Field(..., description="Line color")
    palette_style: str = Field(..., description="Color palette style")
    background: str = Field(..., description="Background description")
    overall_tone: str = Field(..., description="Overall tone of the colors")
    grid_style: str = Field("standard 2x2", description="Grid style")
    gutter_color: str = Field("#FFFFFF", description="Gutter color")
    gutter_width: str = Field("medium", description="Gutter width")
    border_style: str = Field("solid thin line", description="Border style")
    border_color: str = Field("#000000", description="Border color")
    font_hint: Optional[str] = Field("", description="Font style hint")
    bubble_style: Optional[str] = Field("", description="Bubble style hint")


class ComicPrompt(BaseModel):
    """Complete comic prompt with all necessary details."""
    
    id: Optional[str] = Field(None, description="Unique identifier for the prompt")
    created_at: datetime = Field(default_factory=datetime.now, description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")
    
    # Core details
    core_concept: str = Field(..., description="Core concept/theme of the comic")
    narrative_arc: Optional[str] = Field("", description="Narrative arc description")
    reader_feeling: Optional[str] = Field("", description="Target reader feeling")
    
    # Scene details
    overall_scene: str = Field(..., description="Overall scene/environment description")
    comic_title: Optional[str] = Field("", description="Title attempt for the comic")
    content_summary_char: str = Field(..., description="Character(s) in the comic")
    content_summary_action: str = Field(..., description="Core action/content description")
    
    # Reference images
    ref_overall_style: Optional[str] = Field("", description="Overall style reference")
    ref_character: Optional[str] = Field("", description="Character design reference")
    ref_environment: Optional[str] = Field("", description="Environment/item reference")
    ref_pose: Optional[str] = Field("", description="Pose/composition reference")
    ref_other: Optional[str] = Field("", description="Other references")
    
    # Panels and style
    panels: Dict[str, Panel] = Field(..., description="Individual panel details")
    style: StyleProfile = Field(..., description="Comic style profile")
    
    # Generated prompt
    generated_prompt: Optional[str] = Field(None, description="The final generated prompt text")
    
    # User feedback
    is_approved: bool = Field(False, description="Whether the user approved this prompt")
    user_notes: Optional[str] = Field("", description="User notes about this prompt") 