import React from 'react';
import {
  Table,
} from 'react-bootstrap';


class BidAsk extends React.Component {
  render() {
    return (
      <Table striped bordered condensed hover>
        <thead>
          <tr>
            <th>Bid</th>
            <th>Deal</th>
            <th>Ask</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>{ this.props.bid }</td>
            <td>{ this.props.price }</td>
            <td>{ this.props.ask }</td>
          </tr>
        </tbody>
      </Table>
    );
  }
}


export default BidAsk;
