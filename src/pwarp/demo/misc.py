from pwarp import np
from typing import List


def is_close(x, y, vertices, _tol=4):
    vertices_scaled = vertices.copy().astype(int)
    close, index = False, -1

    for i in range(x - _tol, x + _tol):
        for j in range(y - _tol, y + _tol):
            if ([i, j] == vertices_scaled).all(axis=1).any():
                close = True
                click = np.array([i, j])
                index = np.where(np.all(click == vertices_scaled, axis=1))
                index = index[0][0]
                break
    if not close:
        index = -1

    return close, index

def sort_faces(faces: List[List[int]], vertices, focal_point) -> List[List[int]]:
    """
    Sorts a set of faces by decreasing distance from a given focal point
    """
    verts = np.array(vertices)
    centroids = [np.sum(verts[face, :], axis=0)/len(face) for face in faces]
    focal = np.array(focal_point).reshape((1,2))
    diffs = centroids - focal
    dists = np.sum(diffs * diffs, axis=1)
    indices = [i for i in range(len(faces))]
    indices = sorted(indices, key = lambda i: -dists[i])
    return [faces[i] for i in indices]