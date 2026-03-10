"""
Task 1 — Encoding Schemes
Demonstrates ASCII, Base64, Hexadecimal, and URL encoding.
"""

import base64
import binascii
from urllib.parse import quote, unquote


def ascii_info(text: str) -> dict:
    """Return ASCII ordinal values for each character in the input."""
    return {char: ord(char) for char in text if ord(char) < 128}


def base64_encode(data: str) -> str:
    return base64.b64encode(data.encode()).decode()


def base64_decode(data: str) -> str:
    return base64.b64decode(data.encode()).decode()


def hex_encode(data: str) -> str:
    return binascii.hexlify(data.encode()).decode()


def hex_decode(data: str) -> str:
    return binascii.unhexlify(data).decode()


def url_encode(data: str) -> str:
    return quote(data)


def url_decode(data: str) -> str:
    return unquote(data)


def run_demo():
    sample = "Hello, Softwarica! user@email.com"
    print("=" * 50)
    print("TASK 1 — ENCODING SCHEMES")
    print("=" * 50)
    print(f"Input : {sample}\n")

    print("ASCII values:")
    for char, val in ascii_info(sample).items():
        print(f"  '{char}' -> {val}")

    encoded_b64 = base64_encode(sample)
    print(f"\nBase64 Encoded : {encoded_b64}")
    print(f"Base64 Decoded : {base64_decode(encoded_b64)}")

    encoded_hex = hex_encode(sample)
    print(f"\nHex Encoded    : {encoded_hex}")
    print(f"Hex Decoded    : {hex_decode(encoded_hex)}")

    url_sample = "name=Krish Adhikari&college=Softwarica College"
    encoded_url = url_encode(url_sample)
    print(f"\nURL Encoded    : {encoded_url}")
    print(f"URL Decoded    : {url_decode(encoded_url)}")
