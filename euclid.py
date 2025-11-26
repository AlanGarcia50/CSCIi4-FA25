def euclidean_distance(x1, y1, x2, y2):
    
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(euclidean_distance(1, 1, 4, 5)) # Output: 5.0
def euclidean_distance(p1, p2):
    """
    Calculate the Euclidean distance between two points in n-dimensional space.

    Parameters:
    p1 (list): Coordinates of the first point.
    p2 (list): Coordinates of the second point.

    Returns:
    float: The Euclidean distance between the two points.
    """
    squared_differences = [(a - b) ** 2 for a, b in zip(p1, p2)]
    distance = sum(squared_differences) ** 0.5
    return distance
 
    

