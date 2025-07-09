"""Compatibility alias for tests expecting 'src.scraper'."""

import sys
import scraper

# Expose the 'scraper' package as 'src.scraper'
sys.modules.setdefault("src.scraper", scraper)
