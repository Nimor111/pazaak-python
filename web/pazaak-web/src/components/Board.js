import React, {useState, useEffect} from 'react';
import {Button, Row, Col, Container} from 'react-bootstrap';
import './Board.css';

import axios from 'axios';

import CellRow from './CellRow';

const Board = () => {
  const [board, setBoard] = useState([]);

  useEffect(() => {
    nextState('current-state');
  }, []);

  const nextState = async state => {
    const nextBoard = await axios.get(`http://localhost:3000/${state}`);

    setBoard(nextBoard.data.board);
  };

  const halfPoint = Math.floor(board.length / 2);
  const playerBoard = board.slice(0, halfPoint);
  const opponentBoard = board.slice(halfPoint, board.length);

  return (
    <Container>
      <Container>
        <Row>
          <Col>{playerBoard.map(row => <CellRow row={row} />)}</Col>
          <Col>{opponentBoard.map(row => <CellRow row={row} />)}</Col>
        </Row>
      </Container>

      <Row className="mt-4">
        <Button
          className="mr-4"
          variant="primary"
          onClick={() => nextState('next-state')}>
          Next
        </Button>

        <Button variant="danger" onClick={() => nextState('reset')}>
          Reset
        </Button>
      </Row>
    </Container>
  );
};

export default Board;
