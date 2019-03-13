from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

matrix = new_matrix()
print_matrix(matrix)

# print_matrix( make_translate(3, 4, 5) )
# print
# print_matrix( make_scale(3, 4, 5) )
# print
# print_matrix( make_rotX(math.pi/4) )
# print
# print_matrix( make_rotY(math.pi/4) )
# print
# print_matrix( make_rotZ(math.pi/4) )

i = -250
while i < 50:
    add_curve(matrix, 0 + i, 0 + i, 500 + i, 500 + i, 250, 200, 250, 200, 00.1,"bezier")
    draw_lines(matrix,screen,color)
    i += 10

save_extension(screen, 'img.png')
display(screen)

#parse_file( 'script', edges, transform, screen, color )
