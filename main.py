import pymesh
mesh = pymesh.load_mesh("0.off")
print(mesh.num_vertices, mesh.num_faces, mesh.num_voxels)

