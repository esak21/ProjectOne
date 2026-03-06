
from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class packageEvent:
    package_id: Optional[str] = None
    event_type: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None
    time_stamp: Optional[str] = None