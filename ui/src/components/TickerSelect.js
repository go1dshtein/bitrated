import React from 'react';
import {
  MenuItem,
  NavDropdown,
} from 'react-bootstrap';


class TickerSelect extends React.Component {
  constructor(props) {
    super();
  }

  render() {
    const selected = this.props.selected;
    const items = this.props.tickers.map(
      (elem) => (
        <MenuItem
          eventKey={ elem.ticker }
          active={ elem.ticker == selected }
          key={ elem.ticker }
        >
          { elem.ticker }
        </MenuItem>));

    return (
      <NavDropdown
        title={ selected }
        key={ selected }
        id={ "dropdown-basic-tickers" }
        onSelect={(event) => this.props.onSelect(event) }
      >
        { items }
      </NavDropdown>
    );
  }
}


export default TickerSelect;

