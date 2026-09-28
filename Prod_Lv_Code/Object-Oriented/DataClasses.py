'''
Auto-generates __init__, __repr__, __eq__. This is what production codebases use instead of hand-writing boilerplate classes for models/DTOs.
'''

from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    email: str
    is_active: bool = True