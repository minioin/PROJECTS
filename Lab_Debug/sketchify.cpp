#include <cstdlib>
#include <cmath>
#include<iostream>

#include "cs225/PNG.h"
#include "cs225/HSLAPixel.h"
using namespace cs225;
using namespace std;

// sets up the output image
PNG* setupOutput(unsigned w, unsigned h) {
    PNG* image = new PNG(w, h);
    return image;
}

// Returns my favorite color
HSLAPixel* myFavoriteColor(double saturation) {
    HSLAPixel *ptr=new HSLAPixel(159, saturation, 0.5); /*debugged the code here by pointing the pointer to heap memory*/
    return ptr;
}

void sketchify(std::string inputFile, std::string outputFile) {
    // Load in.png
    PNG* original = new PNG(); /*debugged the code here by pointing the pointer to heap memory*/


    original->readFromFile(inputFile);
    unsigned width = original->width();
    unsigned height = original->height();

    // Create out.png
    PNG* output=new PNG();   /*debugged the code here by pointing the pointer to heap memory*/

    output=setupOutput(width, height); /*pointing it to the output file */

    // Load our favorite color to color the outline
    HSLAPixel* myPixel = myFavoriteColor(0.5);

    // Go over the whole image, and if a pixel differs from that to its upper
    // left, color it my favorite color in the output
    for (unsigned y = 1; y<height; y++) {     /*correcting the for loop syntax*/

        for (unsigned x = 1; x<=width-1; x++) {

            // Calculate the pixel difference
            HSLAPixel & prev = original->getPixel(x - 1, y - 1);
            HSLAPixel & curr = original->getPixel(x, y);
            double diff = std::fabs(curr.h - prev.h);

            // If the pixel is an edge pixel,
            // color the output pixel with my favorite color

            HSLAPixel * currOutPixel = &(output->getPixel(x, y));
            if (diff > 20) {
                *currOutPixel = *myPixel;  /*doing the deep copy*/
            }
        }

    }

    // Save the output file
    output->writeToFile(outputFile);

    // Clean up memory
    delete myPixel;
    delete output;
    delete original;


}
