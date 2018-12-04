import React from 'react';
import {
  Navbar,
  Nav,
} from 'react-bootstrap';
import TickerSelect from './TickerSelect';


class SearchBar extends React.Component {
  render() {
    return (
      <Navbar staticTop fluid>
        <Navbar.Header>
          <Navbar.Brand>
            <a href="#home">Bitrate</a>
          </Navbar.Brand>
          <Navbar.Toggle />
        </Navbar.Header>
        <Navbar.Collapse>
          <Nav>
            <TickerSelect
              tickers={ this.props.tickers }
              selected={ this.props.selected }
              onSelect={ this.props.onSelect }
            />
          </Nav>
        </Navbar.Collapse>
      </Navbar>
    );
  }
}


export default SearchBar;
