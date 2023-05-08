"""This module contains functions for interacting with the Twitter API."""
from __future__ import annotations

from . import AutoGPTPushover

plugin = AutoGPTPushover()


def notify_pushover(message: str) -> str:
    """Notify a human with a message.

    Args:
        message (str): The message to send.

    Returns:
        str: The message that was posted.
    """

    _tweetID = plugin.notifier.send_message(message)

    return f"Success! Notified: {message}"

