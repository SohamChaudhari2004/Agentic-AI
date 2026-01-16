import yfinance as yf
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("yfinanceserver")

@mcp.tool()
def stock_price(stock_ticker: str) -> str:
    """
    this tool returns the last known stock price for a given ticker symbol.

    Args: 
        stock_ticker (str): The ticker symbol of the stock.
        Example payload: "AAPL"

    Returns:
        str: "Ticker: Last price"
        Example return: "AAPL: 150.25" 
    """
    data = yf.Ticker(stock_ticker)
    historical_data = data.history(period='1mo') 
    last_month_close = historical_data['Close']
    return f"The current price of {stock_ticker} is {last_month_close}"

if __name__ == "__main__":
    mcp.run(transport='stdio')