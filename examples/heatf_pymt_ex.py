"""An example of operating a Fortran model in PyMT."""

import numpy as np
from pymt.components import Heatf


config_file = 'test.cfg'
np.set_printoptions(precision=1, floatmode='fixed')


# Instantiate the component and get its name.
m = Heatf()
print(m.get_component_name())

# Initialize the model.
m.initialize(config_file)

# List the model's echange items.
print('Input vars:', m.get_input_var_names())
print('Output vars:', m.get_output_var_names())

# Get time information from the model.
print('Start time:', m.get_start_time())
print('End time:', m.get_end_time())
print('Current time:', m.get_current_time())
print('Time step:', m.get_time_step())
print('Time units:', m.get_time_units())

# Advance the model by one time step.
m.update()
print('Update; current time:', m.get_current_time())

# Advance the model by a fractional time step. Not in PyMT?
# m.update_frac(0.75)
# print('Update; current time:', m.get_current_time())

# Advance the model until a later time.
m.update_until(10.0)
print('Update; current time:', m.get_current_time())

# Get the grid_id for the plate_surface__temperature variable.
var_name = 'plate_surface__temperature'
print('Variable {}'.format(var_name))
grid_id = m.get_var_grid(var_name)
print(' - grid id:', grid_id)

# Get grid and variable info for plate_surface__temperature.
print(' - grid type:', m.get_grid_type(grid_id))
grid_rank = m.get_grid_rank(grid_id)
print(' - rank:', grid_rank)
grid_shape = m.get_grid_shape(grid_id)
print(' - shape:', grid_shape)
grid_size = m.get_grid_size(grid_id)
print(' - size:', grid_size)
print(' - spacing:', m.get_grid_spacing(grid_id))
print(' - origin:', m.get_grid_origin(grid_id))
print(' - variable type:', m.get_var_type(var_name))
print(' - units:', m.get_var_units(var_name))
print(' - itemsize:', m.get_var_itemsize(var_name))
print(' - nbytes:', m.get_var_nbytes(var_name))

# Get the temperature values.
val = m.get_value(var_name)
print(' - values (streamwise):')
print(val)
val_gridded = val.reshape(np.roll(grid_shape, 1))
print(' - values (gridded):')
print(val_gridded)

# Set new temperature values.
new = np.arange(grid_size, dtype=np.float32)  # 'real*4 in Fortran
m.set_value(var_name, new)
check = m.get_value(var_name)
print(' - new values (set/get, streamwise):');
print(check)

# Get a reference to the temperature values and check that it updates.
print(' - values (by ref, streamwise) at time {}:'.format(m.get_current_time()))
ref = m.get_value_ptr(var_name)
print(ref)
m.update()
print(' - values (by ref, streamwise) at time {}:'.format(m.get_current_time()))
print(ref)

# Get the grid_id for the plate_surface__thermal_diffusivity variable.
var_name = 'plate_surface__thermal_diffusivity'
print('Variable {}'.format(var_name))
grid_id = m.get_var_grid(var_name)
print(' - grid id:', grid_id)

# Get grid and variable info for plate_surface__thermal_diffusivity.
print(' - grid type:', m.get_grid_type(grid_id))
grid_rank = m.get_grid_rank(grid_id)
print(' - rank:', grid_rank)
print(' - size:', m.get_grid_size(grid_id))
print(' - x:', m.get_grid_x(grid_id))
print(' - y:', m.get_grid_y(grid_id))
print(' - z:', m.get_grid_z(grid_id))
# print(' - connectivity:', m.get_grid_connectivity(grid_id))
# print(' - offset:', m.get_grid_offset(grid_id))
print(' - variable type:', m.get_var_type(var_name))
print(' - units:', m.get_var_units(var_name))
print(' - itemsize:', m.get_var_itemsize(var_name))
print(' - nbytes:', m.get_var_nbytes(var_name))

# Get the diffusivity values.
val = m.get_value(var_name)
print(' - values:')
print(val)

# Get the grid_id for the model__identification_number variable.
var_name = 'model__identification_number'
print('Variable {}'.format(var_name))
grid_id = m.get_var_grid(var_name)
print(' - grid id:', grid_id)

# Get grid and variable info for model__identification_number.
print(' - grid type:', m.get_grid_type(grid_id))
grid_rank = m.get_grid_rank(grid_id)
print(' - rank:', grid_rank)
print(' - size:', m.get_grid_size(grid_id))
print(' - x:', m.get_grid_x(grid_id))
print(' - y:', m.get_grid_y(grid_id))
print(' - z:', m.get_grid_z(grid_id))
# print(' - connectivity:', m.get_grid_connectivity(grid_id))
# print(' - offset:', m.get_grid_offset(grid_id))
print(' - variable type:', m.get_var_type(var_name))
print(' - units:', m.get_var_units(var_name))
print(' - itemsize:', m.get_var_itemsize(var_name))
print(' - nbytes:', m.get_var_nbytes(var_name))

# Get the model id.
val = m.get_value(var_name)
print(' - values:')
print(val)

# Set new model id.
new = 42
m.set_value(var_name, new)
check = m.get_value(var_name)
print(' - new values (set/get):');
print(check)

# Finalize the model.
m.finalize()
