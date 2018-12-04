class TickerService {
  constructor(url) {
    this._url = url;
  }

  getTickerList() {
    const url = this._url + "/api/v1/tickers";
    return this.makeRequest(url);
  }

  getTicker(ticker) {
    const url = this._url + "/api/v1/tickers/" + ticker;
    return this.makeRequest(url);
  }

  getTickerCandles(ticker) {
    const url = this._url + "/api/v1/tickers/" + ticker + "/candles";
    return this.makeRequest(url);
  }

  makeRequest(url) {
    return fetch(url)
      .then((response) => response.json())
      .then((data) => data.data);
  }
};

export default TickerService;
