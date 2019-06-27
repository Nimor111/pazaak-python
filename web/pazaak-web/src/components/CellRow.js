import React from 'react';
import {Row} from 'react-bootstrap';

import Cell from './Cell';

const CellRow = ({row}) => {
  return (
    <div>
      <Row>{row.map(col => <Cell number={col} />)}</Row>
    </div>
  );
};

export default CellRow;
