import numpy as np
import pymt


m = pymt.MODELS.HeatBMI()

args = m.setup(".")
m.initialize(*args)

var_name = m.output_var_names[0]
grid_id = m.var[var_name].grid

val = m.var[var_name].data

val2d = val.reshape(m.grid_shape(grid_id), order="F")
print(val2d)

new_val = np.zeros_like(val)
new_val[20] = 10.0

m.set_value(var_name, new_val)

print(m.var[var_name].data.reshape(m.grid_shape(grid_id), order="F"))

m.update()
print(m.var[var_name].data.reshape(m.grid_shape(grid_id), order="F"))

m.finalize()
