"""This module contains functions for interacting with the Twitter API."""
from __future__ import annotations


from . import AutoGPTSlack

plugin = AutoGPTSlack()


def slack_message(message: str) -> str:
    """Notify a human with a message.

    Args:
        message (str): The message to send.

    Returns:
        str: The message that was posted.
    """

    response = plugin.client.chat_postMessage(
        channel='#bd-agent',
        text=message)
    assert response["message"]["text"] == message

    return f"Success! Slacked: {message}"
