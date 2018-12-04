import React from 'react';
import { render } from 'react-dom';
import Bitrate from './components/Bitrate.js';
import TickerService from './services/TickerService.js'

const apiURL = API_URL;
const TickerServiceInstance = new TickerService(apiURL);

render(
    <Bitrate tickerService={ TickerServiceInstance }/>,
	  document.getElementById('app')
);
