import React from 'react';
import {Card} from 'react-bootstrap';

const Cell = ({number}) => {
  return (
    <Card style={{width: '8rem'}}>
      <Card.Body>
        <Card.Text>{number}</Card.Text>
      </Card.Body>
    </Card>
  );
};

export default Cell;
