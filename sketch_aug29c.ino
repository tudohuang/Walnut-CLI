#include <Adafruit_GFX.h>    // Core graphics library
#include <Adafruit_ILI9341.h> // Hardware-specific library

// Pin definitions for the ILI9341
#define TFT_CLK 13
#define TFT_MISO 12
#define TFT_MOSI 11
#define TFT_CS 10
#define TFT_DC 9
#define TFT_RST 8

Adafruit_ILI9341 tft = Adafruit_ILI9341(TFT_CS, TFT_DC, TFT_RST);



String receivedText;

void setup() {
  tft.begin();
  Serial.begin(9600);
  // Change these to the dimensions of your display
  tft.setRotation(3); // Landscape mode
  tft.fillScreen(ILI9341_BLACK);

  tft.setCursor(0, 0);
  tft.setTextColor(ILI9341_WHITE);
  tft.setTextSize(3);
}

void loop() {
  if (Serial.available() > 0) {
    receivedText = Serial.readStringUntil('\n');  // Read the incoming text
    if (receivedText == "clear") {
      tft.fillScreen(ILI9341_BLACK);  // Clear the screen
      tft.setCursor(0, 0);  // Reset cursor position
    } else {
      // Display the received text on TFT screen
      tft.println(receivedText);
    }
  }
}
