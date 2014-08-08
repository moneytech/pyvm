
#*  nurbs.c
#*  This program shows a NURBS (Non-uniform rational B-splines)
#*  surface, shaped like a heart.

from OpenGL import *

S_NUMPOINTS= 13
S_ORDER    = 3
S_NUMKNOTS = (S_NUMPOINTS + S_ORDER)
T_NUMPOINTS= 3
T_ORDER   =  3
T_NUMKNOTS=  (T_NUMPOINTS + T_ORDER)
SQRT2=    1.41421356237309504880

#* initialized local data *

sknots = -1.0, -1.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 4.0,  5.0,  6.0, 7.0, 8.0, 9.0, 9.0, 9.0
tknots = 1.0, 1.0, 1.0, 2.0, 2.0, 2.0

ctlpoints = (
(   (4.,2.,2.,1.),(4.,1.6,2.5,1.),(4.,2.,3.0,1.)    ),
(   (5.,4.,2.,1.),(5.,4.,2.5,1.),(5.,4.,3.0,1.) ),
(   (6.,5.,2.,1.),(6.,5.,2.5,1.),(6.,5.,3.0,1.) ),
(   (SQRT2*6.,SQRT2*6.,SQRT2*2.,SQRT2),
    (SQRT2*6.,SQRT2*6.,SQRT2*2.5,SQRT2),
    (SQRT2*6.,SQRT2*6.,SQRT2*3.0,SQRT2)  ),
(   (5.2,6.7,2.,1.),(5.2,6.7,2.5,1.),(5.2,6.7,3.0,1.)   ),
(   (SQRT2*4.,SQRT2*6.,SQRT2*2.,SQRT2),
    (SQRT2*4.,SQRT2*6.,SQRT2*2.5,SQRT2),
    (SQRT2*4.,SQRT2*6.,SQRT2*3.0,SQRT2)  ),
(   (4.,5.2,2.,1.),(4.,4.6,2.5,1.),(4.,5.2,3.0,1.)  ),
(   (SQRT2*4.,SQRT2*6.,SQRT2*2.,SQRT2),
    (SQRT2*4.,SQRT2*6.,SQRT2*2.5,SQRT2),
    (SQRT2*4.,SQRT2*6.,SQRT2*3.0,SQRT2)  ),
(   (2.8,6.7,2.,1.),(2.8,6.7,2.5,1.),(2.8,6.7,3.0,1.)   ),
(   (SQRT2*2.,SQRT2*6.,SQRT2*2.,SQRT2),
    (SQRT2*2.,SQRT2*6.,SQRT2*2.5,SQRT2),
    (SQRT2*2.,SQRT2*6.,SQRT2*3.0,SQRT2)  ),
(   (2.,5.,2.,1.),(2.,5.,2.5,1.),(2.,5.,3.0,1.) ),
(   (3.,4.,2.,1.),(3.,4.,2.5,1.),(3.,4.,3.0,1.) ),
(   (4.,2.,2.,1.),(4.,1.6,2.5,1.),(4.,2.,3.0,1.)    )
)

ctlpoints = [x for y in ctlpoints for z in y for x in z]

#*  Initialize material property, light source, lighting model,
#*  and depth buffer.
def myinit():
    global theNurb

    mat_ambient = 1.0, 1.0, 1.0, 1.0
    mat_diffuse = 1.0, 0.2, 1.0, 1.0
    mat_specular = 1.0, 1.0, 1.0, 1.0
    mat_shininess = 50.0,

    light0_position = ( 1.0, 0.1, 1.0, 0.0 )
    light1_position = ( -1.0, 0.1, 1.0, 0.0 )

    lmodel_ambient = ( 0.3, 0.3, 0.3, 1.0 )

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient);
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse);
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular);
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess);
    glLightfv(GL_LIGHT0, GL_POSITION, light0_position);
    glLightfv(GL_LIGHT1, GL_POSITION, light1_position);
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, lmodel_ambient);

    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
    glEnable(GL_LIGHT1);
    glDepthFunc(GL_LESS);
    glEnable(GL_DEPTH_TEST);
    glEnable(GL_AUTO_NORMAL);

    theNurb = gluNewNurbsRenderer();

    gluNurbsProperty(theNurb, GLU_SAMPLING_TOLERANCE, 25.0);
    gluNurbsProperty(theNurb, GLU_DISPLAY_MODE, GLU_FILL);

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glPushMatrix();
    glTranslatef (4., 4.5, 2.5);
    glRotatef (220.0, 1., 0., 0.);
    glRotatef (115.0, 0., 1., 0.);
    glTranslatef (-4., -4.5, -2.5);

    gluBeginSurface(theNurb);
    gluNurbsSurface(theNurb,
	    S_NUMKNOTS, sknots,
	    T_NUMKNOTS, tknots,
	    4 * T_NUMPOINTS,
	    4,
	    ctlpoints,
	    S_ORDER, T_ORDER,
	    GL_MAP2_VERTEX_4);
    gluEndSurface(theNurb);

    glPopMatrix();
    glFlush();

def myReshape(w, h):
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glFrustum(-1.0, 1.0, -1.5, 0.5, 0.8, 10.0);

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(7.0,4.5,4.0, 4.5,4.5,2.0, 6.0,-3.0,2.0);

def key(k, x, y):
    if k == chr (27):
	raise SystemExit

def main():
    import sys
    glutInit();
    glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);
    glutCreateWindow (sys.argv[0]);
    myinit();
    glutReshapeFunc (myReshape);
    glutDisplayFunc(display);
    glutKeyboardFunc(key);
    glutMainLoop();

main ()
