#!/usr/bin/env python3.8
from pwn import *
from typing import Tuple, Mapping
from collections import deque, namedtuple

# we'll use infinity as a default distance to nodes.
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')

def make_edge(start, end, cost=1):
  return Edge(start, end, cost)

class Graph:
    def __init__(self, edges):
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )

    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def dijkstra(self, source, dest, door_times):
        assert source in self.vertices, 'Such source node doesn\'t exist'
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            else:
                while distances[current_vertex] % door_times[current_vertex] != 0:
                    distances[current_vertex] += 1

            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        total_distance = distances[current_vertex]
        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        total_distance = distances[path[-1]]
        return total_distance


def get_tuple(conn: pwnlib.tubes.remote.remote) -> Tuple[int, int]:
    round_ = conn.recvline_regex("[0-9]+ [0-9]+").decode("utf-8").split()
    doors = round_[0]
    paths_ = round_[1]
    return (int(doors), int(paths_))


def get_door_times(conn: pwnlib.tubes.remote.remote) -> Mapping[int, int]:
    round_ = conn.recvline().decode("utf-8").split()
    door_dict = {index+1 : int(round_[index]) for index, _ in enumerate(round_)}
    return door_dict


def get_path_times(conn: pwnlib.tubes.remote.remote, rounds) -> Mapping[int, int]:
    path_listing = []
    for round_ in range(rounds):
        round_ = conn.recvline().decode("utf-8").split()
        path_listing.append((int(round_[0]), int(round_[1]), int(round_[2])))
        # Add it's inverse:
        path_listing.append((int(round_[1]), int(round_[0]), int(round_[2])))
    return Graph(path_listing)

def main():
    conn = remote('142.93.113.55', 31085)
    conn.recvuntil("Type 'start' for try to runaway: ")
    conn.sendline("start")

    for round_ in range(50):
        print(f"Round: {round_}")
        (doors, paths) = get_tuple(conn)
        door_times = get_door_times(conn)
        path_times = get_path_times(conn, paths)
        (start_door, stop_door) = get_tuple(conn)
        distance = path_times.dijkstra(start_door, stop_door, door_times)
        conn.sendline(str(distance))

    # Get flag
    while 1<2:
        try:
            print(conn.recvline().decode("utf-8"))
        except EOFError as e:
            break

if __name__ == '__main__':
    main()
