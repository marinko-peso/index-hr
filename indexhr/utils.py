# -*- coding: utf-8 -*-

_char_mapper = {
    b'\xc4\x8d': b'c', # č
    b'\xc4\x87': b'c', # ć
    b'\xc4\x8c': b'C', # Č
    b'\xc4\x86': b'C', # Ć
    b'\xc5\xa1': b's', # š
    b'\xc5\xa0': b'S', # Š
    b'\xc4\x91': b'd', # đ
    b'\xc4\x90': b'D', # Đ
    b'\xc5\xbe': b'z', # ž
    b'\xc5\xbd': b'Z'  # Ž
}


def clean_text(text):
    """
    sources has issues with all characters outside ascii 256 table so
    manually changing all expected croatian special characters and leaving
    others as "fuzzy" encoded as utf-8.
    """
    text = text.encode('utf-8').strip().replace(b'\n', b'').replace(b'\r', b'')
    for special, new in _char_mapper.items():
        text = text.replace(special, new)
    return text
