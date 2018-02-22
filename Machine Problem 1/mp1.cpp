#include "cs225/PNG.h"
#include "cs225/HSLAPixel.h"
#include <string>
#include <iostream>

using namespace cs225;




void rotate(std::string inputFile, std::string outputFile) {
  // Part 2

  /* creating "png" object for the class PNG and then reading the image from the input files */
  cs225::PNG png;
  png.readFromFile(inputFile);
  HSLAPixel *pixel,*pixel_1;
  HSLAPixel temp;


/* Loop for iteration on image pixel */

for (int x = png.width()-1; x >= (int)(png.width()/2) ; x--) {

    for (int y =png.height()-1; y>=0; y--) {
       /* getting pixels address for the particular coordinates */
       pixel=png.getPixel(x, y);
       pixel_1=png.getPixel(png.width()-1-x,png.height()-1-y);

       /* swapping the required pixel so that image gets rotated by 180 degree */

            temp.l=pixel->l;
            temp.a=pixel->a;
            temp.s=pixel->s;
            temp.h=pixel->h;

            pixel->l=pixel_1->l;
            pixel->a=pixel_1->a;
            pixel->s=pixel_1->s;
            pixel->h=pixel_1->h;

            pixel_1->l=temp.l;
            pixel_1->a=temp.a;
            pixel_1->s=temp.s;
            pixel_1->h=temp.h;



    }

    }

    /* if the width of the image is odd */

if(png.width()%2!=0) {

   unsigned x=png.width()/2;

    for (unsigned y =png.height()-1; y>=png.height()/2; y--) {

               pixel=png.getPixel(x, y);
               pixel_1=png.getPixel(png.width()-1-x,png.height()-1-y);

               temp.l=pixel->l;
               temp.a=pixel->a;
               temp.s=pixel->s;
               temp.h=pixel->h;

               pixel->l=pixel_1->l;
               pixel->a=pixel_1->a;
               pixel->s=pixel_1->s;
               pixel->h=pixel_1->h;

               pixel_1->l=temp.l;
               pixel_1->a=temp.a;
               pixel_1->s=temp.s;
               pixel_1->h=temp.h;
            }
    }

    png.writeToFile(outputFile);
}








PNG myArt(unsigned int width, unsigned int height) {
  PNG png(width, height);
  // Part 3
 /* Loop for iteration on image pixel */


    for (unsigned x = 0; x < png.width(); x++) {

        for (unsigned y = 0; y < png.height(); y++) {

            /* setting luminance /hue /saturation value of pixels to get the required color */

            if(x<png.width()/3 && y<=png.height()/2) {


                HSLAPixel *pixel;
                pixel= png.getPixel(x, y);
                pixel->l=0.8;
                pixel->h=180.0;
                pixel->a=1;
                pixel->s=0.7;
        }
            else if(x>=png.width()/3 && y>png.height()/2) {
                HSLAPixel *pixel;
                pixel= png.getPixel(x, y);
                pixel->l=0.9;
                pixel->h=95.0;
                pixel->a=1;
                pixel->s=0.7;
        }
            else {
                HSLAPixel *pixel;
                pixel= png.getPixel(x, y);
                pixel->l=0.7;
                pixel->h=300.0;
                pixel->a=1;
                pixel->s=0.7;

        }
        }

      }
     return png;
    }
