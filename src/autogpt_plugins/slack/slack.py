"""This module contains functions for interacting with the Twitter API."""
from __future__ import annotations

import pandas as pd
import tweepy

from . import AutoGPTPushover

plugin = AutoGPTPushover()


def notify_pushover(message: str) -> str:
    """Notify a human with a message.

    Args:
        message (str): The message to send.

    Returns:
        str: The message that was posted.
    """

    _tweetID = plugin.notifier.send_message(text=message)

    return f"Success! Notified: {message}"

