import re

def extract_youtube_id(url):
    if not url:
        return None

    patterns = [
        r'youtube\.com/watch\?v=([^&]+)',
        r'youtu\.be/([^?&]+)',
        r'youtube\.com/embed/([^?&]+)',
        r'youtube\.com/shorts/([^?&]+)',
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    return None