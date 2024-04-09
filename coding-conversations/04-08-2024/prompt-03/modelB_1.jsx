// Using Axios in a React component
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function PuzzleComponent() {
  const [puzzle, setPuzzle] = useState(null);

  useEffect(() => {
    const fetchPuzzle = async () => {
      const response = await axios.get('/generate_puzzle');
      setPuzzle(response.data);
    };
    fetchPuzzle();
  }, []);

 //...
}