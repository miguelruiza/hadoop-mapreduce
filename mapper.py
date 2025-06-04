#!/usr/bin/env python3
from textblob import TextBlob
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        _, text, _ = line.split(',', 2)
        text = text.strip('"')
        analysis = TextBlob(text)
        sentiment = analysis.sentiment.polarity
        if sentiment > 0:
            print("positive\t1")
        elif sentiment < 0:
            print("negative\t1")
        else:
            print("neutral\t1")
    except:
        continue
