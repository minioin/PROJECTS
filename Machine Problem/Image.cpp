#include "Image.h"
#include "cs225/HSLAPixel.h"
#include <iostream>
using namespace cs225;
using namespace std;




Image::Image(unsigned int width,unsigned int height):PNG(width,height) {

}


Image::Image():PNG() {
}

void Image::lighten() {


  for (unsigned x = 0; x < this->width(); x++) {
    for (unsigned y = 0; y < this->height(); y++) {
      cs225::HSLAPixel & pixel = this->getPixel(x, y);


      // `pixel` is a pointer to the memory stored inside of the PNG `image`,
      // which means you're changing the image directly.  No need to `set`
      // the pixel since you're directly changing the memory of the image.
      pixel.l = pixel.l +0.1;
      if(pixel.l>1){
        pixel.l=1;
      }
      else if(pixel.l<0) {
        pixel.l=0;
      }
    }
  }
}

void Image::lighten(double amount) {

  for (unsigned x = 0; x < this->width(); x++) {
    for (unsigned y = 0; y < this->height(); y++) {
      cs225::HSLAPixel & pixel = this->getPixel(x, y);


      // `pixel` is a pointer to the memory stored inside of the PNG `image`,
      // which means you're changing the image directly.  No need to `set`
      // the pixel since you're directly changing the memory of the image.
      pixel.l = pixel.l + amount;
      if(pixel.l>1){
        pixel.l=1;
      }
      else if(pixel.l<0) {
        pixel.l=0;
      }
    }
  }
}

void Image::darken() {

    for (unsigned x = 0; x < this->width(); x++) {
    for (unsigned y = 0; y < this->height(); y++) {
     cs225::HSLAPixel & pixel = this->getPixel(x, y);


      // `pixel` is a pointer to the memory stored inside of the PNG `image`,
      // which means you're changing the image directly.  No need to `set`
      // the pixel since you're directly changing the memory of the image.
      pixel.l = pixel.l-0.1;
      if(pixel.l>1){
        pixel.l=1;
      }
      else if(pixel.l<0) {
        pixel.l=0;
      }
    }
  }

}

void Image::darken(double amount) {

        for (unsigned x = 0; x < this->width(); x++) {
    for (unsigned y = 0; y < this->height(); y++) {
      cs225::HSLAPixel & pixel = this->getPixel(x, y);


      // `pixel` is a pointer to the memory stored inside of the PNG `image`,
      // which means you're changing the image directly.  No need to `set`
      // the pixel since you're directly changing the memory of the image.
      pixel.l = pixel.l - amount;
      if(pixel.l>1){
        pixel.l=1;
      }
      else if(pixel.l<0) {
        pixel.l=0;
      }
    }
  }

}


void Image::saturate() {

    for (unsigned x = 0; x < this->width(); x++) {
    for (unsigned y = 0; y < this->height(); y++) {
      cs225::HSLAPixel & pixel = this->getPixel(x, y);


      // `pixel` is a pointer to the memory stored inside of the PNG `image`,
      // which means you're changing the image directly.  No need to `set`
      // the pixel since you're directly changing the memory of the image.
      pixel.s=pixel.s+0.1;
      if(pixel.s>1){
        pixel.s=1;
      }
      else if(pixel.l<0) {
        pixel.s=0;
      }
    }
  }

}

void Image::saturate(double amount){

for (unsigned x = 0; x < this->width(); x++) {
    for (unsigned y = 0; y < this->height(); y++) {
      cs225::HSLAPixel & pixel = this->getPixel(x, y);


      // `pixel` is a pointer to the memory stored inside of the PNG `image`,
      // which means you're changing the image directly.  No need to `set`
      // the pixel since you're directly changing the memory of the image.
      pixel.s=pixel.s+amount;
      if(pixel.s>1){
        pixel.s=1;
      }
      else if(pixel.l<0) {
        pixel.s=0;
      }
    }
  }
}


void Image::desaturate(){

for (unsigned x = 0; x < this->width(); x++) {
    for (unsigned y = 0; y < this->height(); y++) {
      cs225::HSLAPixel & pixel = this->getPixel(x, y);


      // `pixel` is a pointer to the memory stored inside of the PNG `image`,
      // which means you're changing the image directly.  No need to `set`
      // the pixel since you're directly changing the memory of the image.
      pixel.s=pixel.s-0.1;
      if(pixel.s>1){
        pixel.s=1;
      }
      else if(pixel.l<0) {
        pixel.s=0;
      }
    }
  }

}



void Image::desaturate(double amount) {

for (unsigned x = 0; x < this->width(); x++) {
    for (unsigned y = 0; y < this->height(); y++) {
      cs225::HSLAPixel & pixel = this->getPixel(x, y);


      // `pixel` is a pointer to the memory stored inside of the PNG `image`,
      // which means you're changing the image directly.  No need to `set`
      // the pixel since you're directly changing the memory of the image.
      pixel.s=pixel.s-amount;
      if(pixel.s>1){
        pixel.s=1;
      }
      else if(pixel.l<0) {
        pixel.s=0;
      }
    }
  }

}


void Image::grayscale() {

for (unsigned x = 0; x < this->width(); x++) {
    for (unsigned y = 0; y < this->height(); y++) {
      cs225::HSLAPixel & pixel = this->getPixel(x, y);


      // `pixel` is a pointer to the memory stored inside of the PNG `image`,
      // which means you're changing the image directly.  No need to `set`
      // the pixel since you're directly changing the memory of the image.
      pixel.s=0;

    }
  }
}

void Image::rotateColor	(double degrees) {

for (unsigned x = 0; x < this->width(); x++) {
    for (unsigned y = 0; y < this->height(); y++) {
      cs225::HSLAPixel & pixel = this->getPixel(x, y);


      // `pixel` is a pointer to the memory stored inside of the PNG `image`,
      // which means you're changing the image directly.  No need to `set`
      // the pixel since you're directly changing the memory of the image.

      if(degrees>=0) {
        pixel.h=pixel.h+degrees;
      if(pixel.h>360){

        pixel.h=pixel.h-360;
      }
      }
      else {
        pixel.h=pixel.h+degrees;

        if(pixel.h<0) {
           pixel.h=360+pixel.h;

        }


      }

    }
  }

}





void Image::illinify( ) {


for (unsigned x = 0; x < this->width(); x++) {
for (unsigned y = 0; y < this->height(); y++) {

                cs225::HSLAPixel & pixel = this->getPixel(x, y);
                // pixel` is a pointer to the memory stored inside of the PNG `image`,
                // which means you're changing the image directly.  No need to `set`
                // the pixel since you're directly changing the memory of the image.

                if(pixel.h>=11 && pixel.h<=216) {
                    if((pixel.h-11) > (216-pixel.h)) {
                           pixel.h=216;  }
                    else {
                           pixel.h=11;
                     }
                     }
                else if (pixel.h>=0 && pixel.h<11) {
                           pixel.h=11;
                        }
                else {
                    if((pixel.h-216) > (360-pixel.h+11)) {
                           pixel.h=11;
                     }
                    else {
                           pixel.h=216;
                     }
                     }
        }
    }
}


void Image::scale(double factor) {



        unsigned newwidth=factor*this->width();
        unsigned newheight=factor*this->height();
        Image newImg(newwidth, newheight);


    for (unsigned x = 0; x < newwidth; x++) {
    for (unsigned y = 0; y < newheight; y++) {

    unsigned int oldx=( unsigned int)(x/factor);
    unsigned int oldy=( unsigned int)(y/factor);


      cs225::HSLAPixel & oldPixel = this->getPixel(oldx,oldy);
      cs225::HSLAPixel & newPixel = newImg.getPixel(x,y);
      newPixel=oldPixel;
        }
    }

    *this=newImg;
}


void Image::scale(unsigned w,unsigned h )  {

    double f1=(double)w/this->width();
    double f2=(double)h/this->height();
    if(f1>f2) {

        scale(f2);
    }
    else{

        scale(f1);
    }
}







