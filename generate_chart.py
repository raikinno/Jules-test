import yfinance as yf
import mplfinance as mpf
import datetime

def generate_sp500_chart():
    """
    過去1年間のS&P500の過去データを取得し、ローソク足チャートとして保存します。
    """
    # S&P500のティッカーシンボルを定義します
    ticker_symbol = "^GSPC"

    # S&P500のデータを取得します
    ticker_data = yf.Ticker(ticker_symbol)

    # 過去1年間の過去データを取得します
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=365)

    hist_data = ticker_data.history(start=start_date, end=end_date)

    # データが正常に取得できたか確認します
    if hist_data.empty:
        print("S&P500のデータを取得できませんでした。休日または週末の可能性があります。")
        return

    # ローソク足チャートを生成して保存します
    mpf.plot(
        hist_data,
        type='candle',
        style='charles',
        title='S&P 500 Candlestick Chart (Last Year)',
        ylabel='Price ($)',
        volume=True,
        ylabel_lower='Volume',
        savefig='sp500_chart.png'
    )
    print("S&P 500のチャートが生成され、sp500_chart.pngとして保存されました。")

if __name__ == "__main__":
    generate_sp500_chart()
