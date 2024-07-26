def non_bot_non_self(filter, client, message):
    return not message.from_user.is_bot and message.from_user.id != client.me.id