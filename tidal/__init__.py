def SEACH_API(**e):
    return f'https://tidal.401658.xyz/search/?s={e.get("title")}&a={e.get("artist", "")}&al={e.get("album", "")}'