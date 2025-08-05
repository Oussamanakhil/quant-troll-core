# Data Notes

## OHLCV
Source: CryptoDataDownload (1min, 15min, daily)
Format: CSV — stored under /data/

## Sentiment
Source: SNScrape (Twitter), CryptoPanic (News)

## Derivatives
Planned: CryptoQuant (Funding, OI)
To add: Hyblock (liquidation heatmaps)

## Integrity Check
All datasets will be checked for:
- Missing timestamps
- NaNs
- Timezone alignment
