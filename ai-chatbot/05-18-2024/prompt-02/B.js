class Graph {
  constructor() {
    this.adjacencyList = {};
  }

  addVertex(vertex) {
    if (!this.adjacencyList[vertex]) {
      this.adjacencyList[vertex] = [];
    }
  }

  addEdge(vertex1, vertex2) {
    if (this.adjacencyList[vertex1] && this.adjacencyList[vertex2]) {
      this.adjacencyList[vertex1].push(vertex2);
      this.adjacencyList[vertex2].push(vertex1);
    }
  }

  DFS(startingVertex) {
    const visited = new Set();
    const result = [];

    function dfsHelper(vertex) {
      visited.add(vertex);
      result.push(vertex);

      for (const neighbor of this.adjacencyList[vertex]) {
        if (!visited.has(neighbor)) {
          dfsHelper.call(this, neighbor);
        }
      }
    }

    dfsHelper.call(this, startingVertex);
    return result;
  }

  BFS(startingVertex) {
    const visited = new Set();
    const queue = [startingVertex];
    const result = [];

    while (queue.length > 0) {
      const currentVertex = queue.shift();
      if (!visited.has(currentVertex)) {
        visited.add(currentVertex);
        result.push(currentVertex);

        for (const neighbor of this.adjacencyList[currentVertex]) {
          if (!visited.has(neighbor)) {
            queue.push(neighbor);
          }
        }
      }
    }

    return result;
  }
}

// Example usage:
const graph = new Graph();
graph.addVertex('A');
graph.addVertex('B');
graph.addVertex('C');
graph.addVertex('D');
graph.addEdge('A', 'B');
graph.addEdge('A', 'C');
graph.addEdge('B', 'D');
graph.addEdge('C', 'D');

console.log(graph.DFS('A')); // Output: ['A', 'B', 'D', 'C']
console.log(graph.BFS('A')); // Output: ['A', 'B', 'C', 'D']