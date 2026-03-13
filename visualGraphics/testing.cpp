//
// Created by Drew on 11/23/2025.
//

#include <GL/glut.h>

void display() {
    // Clear screen (color buffer only)
    glClear(GL_COLOR_BUFFER_BIT);

    // Set drawing color (R, G, B)
    glColor3f(1.0f, 0.0f, 0.0f);

    // Draw simple triangle
    glBegin(GL_TRIANGLES);
    glVertex2f(-0.5f, -0.5f);
    glVertex2f( 0.5f, -0.5f);
    glVertex2f( 0.0f,  0.5f);
    glEnd();

    // Send to screen
    glFlush();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);               // Initialize GLUT
    glutCreateWindow("Simple GLUT");     // Create window
    glutDisplayFunc(display);            // Set display callback
    glutMainLoop();                      // Start event loop (infinite)
    return 0;
}
