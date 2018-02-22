#include "Image.h"
#include "StickerSheet.h"


int main() {

  Image alma;
  alma.readFromFile("alma.png");
  StickerSheet sheet(alma, 100);

  Image wade,css225,test_case,welcome;


  wade.readFromFile("wade.png");
  css225.readFromFile("css225.png");
  test_case.readFromFile("test_case.png");
  welcome.readFromFile("WELCOME.png");


  wade.scale(0.5);
  welcome.scale(0.5);

  css225.scale(0.5);
  test_case.scale(0.5);
  sheet.addSticker(wade, 0, 0);
  sheet.addSticker(css225, 635,200);
  sheet.addSticker(test_case,100,500);
  sheet.addSticker(welcome,635,100);
  Image result=sheet.render();
  result.writeToFile("myImage.png");





  //
  // Reminder:
  //   Before exiting main, save your creation to disk as myImage.png
  //

  return 0;
}
