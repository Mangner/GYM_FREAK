from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.party import Party


class IMessageService(ABC):
    """Abstract messaging contract.

    The `recipient` can be a `Person` or an `Organization` (both inherit from `Party`).
    Implementations handle routing automatically based on the concrete party type.
    """

    @abstractmethod
    def send_message(self, sender: "Party", recipient: "Party", content: str) -> bool:
        raise NotImplementedError
