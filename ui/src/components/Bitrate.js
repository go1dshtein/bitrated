import React from 'react';
import { Button, Grid, Row, Col } from 'react-bootstrap';

import SearchBar from './SearchBar.js';
import Chart from './Chart.js';
import BidAsk from './BidAsk.js';

class Bitrate extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        tickers: [{ticker: "BTCUSD"}],
        selected: "BTCUSD",
        rate: null,
        candles: null
      };
    }
    componentDidMount() {
      this.props.tickerService.getTickerList()
        .then((data) => this.setState({tickers: data}));
      this.refreshRate(this.state.selected);
      this.refreshCandles(this.state.selected);
    }

    refreshRate(selected) {
      this.props.tickerService.getTicker(selected)
        .then((data) => this.setState({rate: data}));
    }

    refreshCandles(selected) {
      this.props.tickerService.getTickerCandles(selected)
        .then((data) => this.setState({candles: data}));
    }

    onSelectTicker(selected) {
      this.setState({selected: selected});
      this.refreshRate(selected);
      this.refreshCandles(selected);
    }

    render() {
      const chart = (!this.state.candles) ? null : (
        <Chart
          type={ "hybrid" }
          data={ this.state.candles }
          ticker={ this.state.selected }
        />
      );

      const bidask = (!this.state.rate) ? null : (
        <BidAsk
          bid={ this.state.rate.bid }
          ask={ this.state.rate.ask }
          price={ this.state.rate.price }
        />
      );
    	return (
        <div>
          <SearchBar
            tickers={ this.state.tickers }
            selected={ this.state.selected }
            onSelect={ this.onSelectTicker.bind(this) }
          />
          <Grid>
            <Row>
              <Col xs={12} md={6}>
                { bidask }
              </Col>
            </Row>
            <Row>
              <Col xs={12} md={8}>
                { chart }
              </Col>
            </Row>
          </Grid>
    	  </div>);
    }
}

export default Bitrate;
