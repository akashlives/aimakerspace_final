from datetime import datetime, timedelta
from config import MEMORY_RESET_INTERVAL_MINUTES

memory_reset_interval = timedelta(minutes=MEMORY_RESET_INTERVAL_MINUTES)
user_last_interaction = {}
user_memory = {}


def get_user_memory(user_id):
    """
    Retrieves the memory for a given user.

    If the user's last interaction was within the memory reset interval,
    it returns the existing memory. Otherwise, it resets the memory and
    updates the last interaction time.

    Args:
        user_id (str): The unique identifier for the user.

    Returns:
        list: The user's memory as a list of messages.
    """
    now = datetime.now()
    last_interaction = user_last_interaction.get(user_id)

    if last_interaction and (now - last_interaction) < memory_reset_interval:
        return user_memory.get(user_id, [])
    else:
        user_memory[user_id] = []
        user_last_interaction[user_id] = now
        return user_memory[user_id]


def update_user_memory(user_id, message):
    """
    Updates the memory for a given user with a new message.

    This function adds the new message to the user's memory and
    updates the last interaction time.

    Args:
        user_id (str): The unique identifier for the user.
        message (str): The message to be added to the user's memory.
    """
    now = datetime.now()
    user_last_interaction[user_id] = now
    user_memory[user_id].append(message)
