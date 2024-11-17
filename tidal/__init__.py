def SEACH_API(**e):
    return f'https://tidal.401658.xyz/search/?s={e.get("title")}&a={e.get("artist", "")}&al={e.get("album", "")}'

def TRACK_API(**e):
    return f'https://tidal.401658.xyz/track/?id={e.get("id")}&quality={e.get('quality', 'HIGH')}'