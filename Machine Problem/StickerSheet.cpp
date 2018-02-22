#include "StickerSheet.h"
#include "Image.h"
#include "cs225/HSLAPixel.h"
#include "cs225/PNG.h"
#include<iostream>
using namespace std;
using namespace cs225;

StickerSheet::StickerSheet(const Image & picture,unsigned max )
{
    base=new Image(picture);
    size=max;
    IM=new Image*[size];
    for(unsigned i=0;i<size;i++) {
    IM[i]=NULL;
    }
    xarray=new unsigned[size];

    yarray=new unsigned[size];



}



StickerSheet::StickerSheet(const StickerSheet & other) {
        this->base=new Image(*(other.base));
        this->size=other.size;

        IM=new Image*[other.size];

        this->xarray=new unsigned[other.size];

        this->yarray=new unsigned[other.size];



        for(unsigned i=0;i<other.size;i++) {
                if(other.IM[i]!=NULL){
                     IM[i]= new Image(*(other.IM[i]));
                     xarray[i]=other.xarray[i];
                     yarray[i]=other.yarray[i];
                 }

                else {
                     IM[i]=NULL;
                     }
        }

  }




const StickerSheet& StickerSheet::operator=(const StickerSheet & other)	{

      for(unsigned i=0;i<size;i++) {
              if(IM[i]!=NULL){
                  delete IM[i];
              }
          }

      delete [] IM;

      delete [] xarray;
      delete [] yarray;
      delete base;
      IM=NULL;
      xarray=NULL;
      yarray=NULL;
      base=NULL;
      this->base=new Image(*(other.base));
      this->size=other.size;

       IM=new Image*[other.size];

        this->xarray=new unsigned[other.size];

        this->yarray=new unsigned[other.size];



        for(unsigned i=0;i<other.size;i++) {
                if(other.IM[i]!=NULL){
                     IM[i]= new Image(*(other.IM[i]));
                     xarray[i]=other.xarray[i];
                     yarray[i]=other.yarray[i];
                 }

                else {
                     IM[i]=NULL;
                     }
        }
     return *this;
}





void StickerSheet::changeMaxStickers(unsigned max) {
/*
if(max<0) {
    return;
}*/

if(max>size) {
  Image **temp=new Image*[max];
  unsigned *xtemp=new unsigned[max];
  unsigned *ytemp=new unsigned[max];
for(unsigned i=0;i<max;i++) {
    temp[i]=NULL;
}

for(unsigned i=0;i<size;i++) {
    temp[i]=IM[i];
    xtemp[i]=xarray[i];
    ytemp[i]=yarray[i];
 }
 delete []xarray;
 delete []yarray;


 delete [] IM;

 size=max;
 IM=temp;
 xarray=xtemp;
 yarray=ytemp;
}
else if (size>max){

  Image **temp=new Image*[max];
  unsigned *xtemp=new unsigned[max];
  unsigned *ytemp=new unsigned[max];
for(unsigned i=max;i<size;i++){

    delete IM[i];

}
for(unsigned i=0;i<max;i++) {
    temp[i]=NULL;
}

 for(unsigned i=0;i<max;i++) {
    temp[i]=IM[i];
    xtemp[i]=xarray[i];
    ytemp[i]=yarray[i];
 }


delete []xarray;
delete []yarray;


delete [] IM;
xarray=xtemp;
yarray=ytemp;

 size=max;
 IM=temp;

}




}




int StickerSheet::addSticker(Image & sticker,unsigned x,unsigned y) {



for(unsigned i=0;i<size;i++) {
    if(IM[i]==NULL){
    IM[i]=new Image(sticker);
    xarray[i]=x;
    yarray[i]=y;
    return i;
    }
}
return -1;

}


bool StickerSheet::translate(unsigned index,unsigned x,unsigned y) {


for(unsigned i=0;i<size;i++) {

if(i==index && IM[i]!=NULL) {
xarray[index]=x;
yarray[index]=y;
return true;
} }

return false;
}


void StickerSheet::removeSticker(unsigned index) {

for(unsigned i=0;i<size;i++) {

if(i==index && IM[i]!=NULL) {

delete IM[index];

IM[index]=NULL;
break;

}
} }



Image StickerSheet::render() const  {

unsigned width_pic=base->width();
unsigned height_pic=base->height();


  for(unsigned i=0;i<size;i++) {
                  if(IM[i]!=NULL) {

                     unsigned width_x=xarray[i]+IM[i]->width();
                     unsigned height_y=yarray[i]+IM[i]->height();
                          if(width_x>width_pic) {
                                width_pic=width_x;
                             }
                          if(height_y>height_pic) {
                            height_pic=height_y;
                            }
                           base->resize(width_pic,height_pic);
                           for(unsigned j=0;j<IM[i]->width();j++){
                                for(unsigned k=0;k<IM[i]->height();k++) {

                                   if(IM[i]->getPixel(j,k).a !=0) {
                                      base->getPixel(xarray[i]+j,yarray[i]+k)=IM[i]->getPixel(j,k);

                            }
                        }
                    }
                }

                }
        return *base;

    }




Image* StickerSheet::getSticker(unsigned index) const {

for(unsigned i=0;i<size;i++) {
        if(i==index && IM[i]!=NULL){
    return IM[i];
}
}
return NULL;
}


StickerSheet::~StickerSheet ()
{

 for(unsigned i = 0; i<size; i++){
		if(IM[i]!=NULL){
			delete IM[i];
			IM[i]=NULL;
		}
	}
	delete[] IM;
	delete[] xarray;
	delete[] yarray;
	IM = NULL;
	xarray = NULL;
	yarray = NULL;
	delete base;
	base=NULL;
}







