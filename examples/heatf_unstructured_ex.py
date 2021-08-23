"""An example of calling a Fortran BMI through Cython."""

import numpy as np
from pymt_heatf import Heatf


config_file = "test.cfg"


# Instantiate a model and get its name.
m = Heatf()
print(m.get_component_name())

# Initialize the model.
m.initialize(config_file)

# Get the grid_id for the plate_surface__temperature variable.
var_name = "plate_surface__temperature"
print("Variable {}".format(var_name))
grid_id = m.get_var_grid(var_name)
print(" - grid id:", grid_id)

# Get grid and variable info for plate_surface__temperature.
# All should raise RuntimeError because they're not implemented.
node_count = m.get_grid_node_count(grid_id)
edge_count = m.get_grid_edge_count(grid_id)
face_count = m.get_grid_face_count(grid_id)
print(" - node count:", node_count)
print(" - edge count:", edge_count)
print(" - face count:", face_count)

nodes_per_face = np.empty(face_count, dtype=np.int32)
m.get_grid_nodes_per_face(grid_id, nodes_per_face)
print(" - nodes per face:", nodes_per_face)

edge_nodes = np.empty(2 * edge_count, dtype=np.int32)
m.get_grid_edge_nodes(grid_id, edge_nodes)
print(" - edge nodes:", edge_nodes)

face_edges = np.empty(np.sum(nodes_per_face), dtype=np.int32)
m.get_grid_face_edges(grid_id, face_edges)
print(" - face edges:", face_edges)

face_nodes = np.empty(np.sum(nodes_per_face), dtype=np.int32)
m.get_grid_face_nodes(grid_id, face_nodes)
print(" - face nodes:", face_nodes)


# print(' - grid type:', m.get_grid_type(grid_id))
# grid_rank = m.get_grid_rank(grid_id)
# print(' - rank:', grid_rank)
# grid_shape = np.empty(grid_rank, dtype=np.int32)
# m.get_grid_shape(grid_id, grid_shape)
# print(' - shape:', grid_shape)
# grid_size = m.get_grid_size(grid_id)
# print(' - size:', grid_size)
# grid_spacing = np.empty(grid_rank, dtype=np.float64)
# m.get_grid_spacing(grid_id, grid_spacing)
# print(' - spacing:', grid_spacing)
# grid_origin = np.empty(grid_rank, dtype=np.float64)
# m.get_grid_origin(grid_id, grid_origin)
# print(' - origin:', grid_origin)
# print(' - variable type:', m.get_var_type(var_name))
# print(' - units:', m.get_var_units(var_name))
# print(' - itemsize:', m.get_var_itemsize(var_name))
# print(' - nbytes:', m.get_var_nbytes(var_name))
# print(' - location:', m.get_var_location(var_name))

# Finalize the model.
m.finalize()
