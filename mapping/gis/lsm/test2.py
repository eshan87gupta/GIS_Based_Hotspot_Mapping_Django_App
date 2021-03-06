import numpy as np

cy = np.linspace(0, 10, 5) # [ 0. , 2.5 , 5. , 7.5 , 10.]


cx = np.linspace(0, 10, 5) # [ 0. , 2.5 , 5. , 7.5 , 10.]



cx_grid, cy_grid = np.meshgrid(cx, cy)

# cx_grid : [[ 0.   2.5  5.   7.5 10. ],[ 0.   2.5  5.   7.5 10. ],[ 0.   2.5  5.   7.5 10. ],[ 0.   2.5  5.   7.5 10. ],[ 0.   2.5  5.   7.5 10. ]]
# cx_grid.shape : (5, 5)
# cy_grid : [[ 0.   0.   0.   0.   0. ],[ 2.5  2.5  2.5  2.5  2.5],[ 5.   5.   5.   5.   5. ],[ 7.5  7.5  7.5  7.5  7.5],[10.  10.  10.  10.  10. ]]
# cx_grid.shape : (5, 5)

print(cx_grid,'\n',np.expand_dims(cx_grid, 0),'\n',np.expand_dims(cx_grid, 1))
cx_grid = np.expand_dims(cx_grid, -1)
cy_grid = np.expand_dims(cy_grid, -1)

# cx_grid : [[[ 0. ],[ 2.5],[ 5. ],[ 7.5],[10. ]],[[ 0. ],[ 2.5],[ 5. ],[ 7.5],[10. ]],[[ 0. ],[ 2.5],[ 5. ],[ 7.5],[10. ]],
# [[ 0. ],[ 2.5],[ 5. ],[ 7.5],[10. ]],[[ 0. ],[ 2.5],[ 5. ],[ 7.5],[10. ]]]
#print(cx_grid)


# cy_grid : [[[ 0. ],[ 0. ],[ 0. ],[ 0. ],[ 0. ]],[[ 2.5],[ 2.5],[ 2.5],[ 2.5],[ 2.5]],[[ 5. ],[ 5. ],[ 5. ],[ 5. ],[ 5. ]]
# [[ 7.5],[ 7.5],[ 7.5],[ 7.5],[ 7.5]],[[10. ],[10. ],[10. ],[10. ],[10. ]]]

#print(np.tile(cx_grid, (1, 1, 2)))
cx1 = np.tile(cx_grid, (1, 1, 2))

# [[[ 0.   0. ],[ 2.5  2.5],[ 5.   5. ],[ 7.5  7.5],[10.  10. ]],
# [[ 0.   0. ],[ 2.5  2.5],[ 5.   5. ],[ 7.5  7.5],[10.  10. ]],
# [[ 0.   0. ],[ 2.5  2.5],[ 5.   5. ],[ 7.5  7.5],[10.  10. ]],
# [[ 0.   0. ],[ 2.5  2.5],[ 5.   5. ],[ 7.5  7.5],[10.  10. ]]
# [[ 0.   0. ],[ 2.5  2.5],[ 5.   5. ],[ 7.5  7.5],[10.  10. ]]]

#print(np.tile(cy_grid, (1, 1, 2)))
cx2 = np.tile(cy_grid, (1, 1, 2))

# [[[ 0.   0. ],[ 0.   0. ],[ 0.   0. ],[ 0.   0. ],[ 0.   0. ]],
# [[ 2.5  2.5],[ 2.5  2.5],[ 2.5  2.5],[ 2.5  2.5],[ 2.5  2.5]]
# [[ 5.   5. ],[ 5.   5. ],[ 5.   5. ],[ 5.   5. ],[ 5.   5. ]]
# [[ 7.5  7.5],[ 7.5  7.5],[ 7.5  7.5],[ 7.5  7.5],[ 7.5  7.5]]
# [[10.  10. ],[10.  10. ],[10.  10. ],[10.  10. ],[10.  10. ]]]



#print(cx1[...,0])