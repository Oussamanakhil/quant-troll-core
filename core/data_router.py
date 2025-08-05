def load_ohlcv(pair: str, source: str = "CryptoDataDownload", freq: str = "15m"):
    if source == "CryptoDataDownload":
        return pd.read_csv(f"data/{pair}_{freq}.csv", parse_dates=["datetime"])
    elif source == "Binance":
        # Placeholder for ccxt fetch
        return fetch_from_binance(pair, freq)
    elif source == "AlphaVantage":
        return fetch_from_alpha_vantage(pair)
    else:
        raise ValueError("Unknown OHLCV source")

def load_sentiment(source: str = "SNScrape"):
    if source == "SNScrape":
        return pd.read_csv("data/sentiment_score.csv", parse_dates=["timestamp"])
    elif source == "CryptoPanic":
        return fetch_cryptopanic_news()
