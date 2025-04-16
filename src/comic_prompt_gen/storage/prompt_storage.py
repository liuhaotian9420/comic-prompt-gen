"""Storage functionality for saving and loading user prompts."""
import os
import json
import uuid
from datetime import datetime
from typing import Dict, List, Optional
from pathlib import Path

import streamlit as st

from ..core.models import ComicPrompt


class PromptStorage:
    """Storage manager for comic prompts."""
    
    def __init__(self, storage_dir: str = "saved_prompts"):
        """Initialize the storage manager.
        
        Args:
            storage_dir: Directory to store prompt files
        """
        self.storage_dir = Path(storage_dir)
        # Create storage directory if it doesn't exist
        self.storage_dir.mkdir(parents=True, exist_ok=True)
    
    def save_prompt(self, prompt: ComicPrompt) -> str:
        """Save a prompt to storage.
        
        Args:
            prompt: The ComicPrompt object to save
            
        Returns:
            The ID of the saved prompt
        """
        # Generate ID if not present
        if prompt.id is None:
            prompt.id = str(uuid.uuid4())
        
        # Update timestamp
        prompt.updated_at = datetime.now()
        
        # Prepare filename
        filename = f"{prompt.id}.json"
        filepath = self.storage_dir / filename
        
        # Save to file
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(prompt.model_dump(), f, default=str, ensure_ascii=False, indent=2)
        
        return prompt.id
    
    def load_prompt(self, prompt_id: str) -> Optional[ComicPrompt]:
        """Load a prompt from storage.
        
        Args:
            prompt_id: The ID of the prompt to load
            
        Returns:
            The loaded ComicPrompt object, or None if not found
        """
        filepath = self.storage_dir / f"{prompt_id}.json"
        
        if not filepath.exists():
            return None
        
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                return ComicPrompt.model_validate(data)
        except Exception as e:
            st.error(f"Error loading prompt: {e}")
            return None
    
    def list_prompts(self) -> List[Dict]:
        """List all saved prompts with basic metadata.
        
        Returns:
            List of prompt metadata (id, title, creation date)
        """
        prompts = []
        
        for file in self.storage_dir.glob("*.json"):
            try:
                with open(file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    prompts.append({
                        "id": data.get("id"),
                        "core_concept": data.get("core_concept", "Untitled"),
                        "created_at": data.get("created_at"),
                        "is_approved": data.get("is_approved", False)
                    })
            except Exception:
                # Skip invalid files
                continue
        
        # Sort by creation date, newest first
        prompts.sort(key=lambda x: x.get("created_at", ""), reverse=True)
        return prompts
    
    def delete_prompt(self, prompt_id: str) -> bool:
        """Delete a prompt from storage.
        
        Args:
            prompt_id: The ID of the prompt to delete
            
        Returns:
            True if deleted successfully, False otherwise
        """
        filepath = self.storage_dir / f"{prompt_id}.json"
        
        if not filepath.exists():
            return False
        
        try:
            filepath.unlink()
            return True
        except Exception:
            return False


# Create a session-based storage instance
def get_storage() -> PromptStorage:
    """Get the PromptStorage instance (creates one if needed).
    
    Returns:
        The PromptStorage instance
    """
    if "prompt_storage" not in st.session_state:
        st.session_state.prompt_storage = PromptStorage()
    
    return st.session_state.prompt_storage 