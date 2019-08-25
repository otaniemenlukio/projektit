#include <Wire.h>
#include <LiquidCrystal_I2C.h>

#define NUMBER_OF_QUESTIONS 3
#define NUMBER_OF_ANSWERS 4

#define ae 0
#define oe 1
#define AE 2
#define up 4
#define down 5
#define left 127
#define right 126

const String questions[][3] = {
  {"Mikä seuraavista", "ei ole kuolevaa", "kohtaava kiusaus?"},
  {"Kuka yhdisti", "antiikin filosofian", "ja teologian?"},
  {"Mikä oli Edward IV:n", "ruttoläkkeen kes-", "keisin ainesosa?"},
};
const String answers[][NUMBER_OF_ANSWERS][2] = {
  {
    {"Epätoivo"},
    {"Saituruus"},
    {"Kateus"},
    {"Kärsimättömyys"},
  },
  {
    {"Kuningas", "Edward IV"},
    {"Tuomas", "Akvinolainen"},
    {"Guy de", "Chauliac"},
    {"Paavi", "Klemens VI"},
  },
  {
    {"Kananmuna"},
    {"Hevosen", "veri"},
    {"Piparjuuri"},
    {"Minttu"},
  },
};

const int correct[] = {
  2,
  1,
  0,
};

uint8_t ae_glyph[8]  = {
  B01010,
  B00000,
  B01110,
  B00001,
  B01111,
  B10001,
  B01111,
  B00000
};
uint8_t oe_glyph[8]  = {
  B01010,
  B00000,
  B01110,
  B10001,
  B10001,
  B10001,
  B01110,
  B00000
};
uint8_t AE_glyph[8] = {
  B01010,
  B00000,
  B01110,
  B10001,
  B11111,
  B10001,
  B10001,
  B00000
};
uint8_t up_glyph[8]  = {
  B00000,
  B00100,
  B01110,
  B10101,
  B00100,
  B00100,
  B00100,
  B00000
};
uint8_t down_glyph[8]  = {
  B00000,
  B00100,
  B00100,
  B00100,
  B10101,
  B01110,
  B00100,
  B00000
};

LiquidCrystal_I2C lcd(0x27, 20, 4); // set the LCD address to 0x27 for a 16 chars and 2 line display

// lcd.print() but with äö compatibility
void showText(String content) {
  for (int pos = 0; pos < content.length(); pos++) {
    String character = content.substring(pos, pos + 2);
    if (character == "ä") {
      lcd.write(ae);
      pos++;
    } else if (character == "Ä") {
      lcd.write(AE);
      pos++;
    } else if ((character == "Ö") or (character == "ö")) {
      lcd.write(oe);
      pos++;
    } else {
      lcd.print(content[pos]);
    }

  }
}

int waitJoystick() {
  while (1) {
    if (!digitalRead(2)) {
      while (!digitalRead(2)) {
        delay(50);
      } return 0;
    }
    if (analogRead(A2) > 1000) {
      while (analogRead(A2) > 800) {
        delay(50);
      } return 3;
    }
    if (analogRead(A3) < 20) {
      while (analogRead(A3) < 200) {
        delay(50);
      } return 2;
    }
    if (analogRead(A3) > 1000) {
      while (analogRead(A3) > 800) {
        delay(50);
      } return 4;
    }
    if (analogRead(A2) < 20) {
      while (analogRead(A2) < 200) {
        delay(50);
      } return 1;
    }
  }
}

void question(int number) {
  lcd.clear();
  lcd.print("Kysymys ");
  lcd.print(number + 1);
  for (int row = 0; row < 3; row++) {
    lcd.setCursor(0, row + 1);
    showText(questions[number][row]);
  }

  lcd.setCursor(19, 3);
  lcd.write(right);
  while (waitJoystick() != 1) {}
}

bool answer(int number) {
  question(number);
  int selection = -1;
  int current = 0;
  while (selection == -1) {
    lcd.clear();
    lcd.setCursor(0, 1);
    lcd.write(65 + current);
    lcd.print(")");
    for (int row = 0; row < 2; row++) {
      lcd.setCursor(3, row + 1);
      showText(answers[number][current][row]);
    }
    if (current < NUMBER_OF_ANSWERS - 1) {
      lcd.setCursor(19, 3);
      lcd.write(down);
    }
    if (current > 0) {
      lcd.setCursor(19, 0);
      lcd.write(up);
    }
    lcd.setCursor(0, 3);
    lcd.write(left);

    int userInput = waitJoystick();
    if (userInput == 2) {
      current = min(NUMBER_OF_ANSWERS - 1, current + 1);
    } else if (userInput == 4) {
      current = max(0, current - 1);
    } else if (userInput == 0) {
      selection = current;
    } else if (userInput == 3) {
      question(number);
    }
  }
  return (selection == correct[number]);
}

void setup()
{
  pinMode(2, INPUT_PULLUP);
  lcd.init();                      // initialize the lcd
  lcd.backlight();

  lcd.createChar(ae, ae_glyph);
  lcd.createChar(oe, oe_glyph);
  lcd.createChar(AE, AE_glyph);
  lcd.createChar(up, up_glyph);
  lcd.createChar(down, down_glyph);
  lcd.clear();
  Serial.begin(9600);
}

void loop()
{
  bool winning = true;
  
  for (int i = 0; i < NUMBER_OF_QUESTIONS; i++) {
    winning = answer(i) && winning;
  }
  
  if (winning) {
    lcd.clear();
    showText("Onnittelut! Vastasit");
    lcd.setCursor(0,1);
    showText("kysymyksiin oikein.");
    lcd.setCursor(0,3);
    showText(" ");
    for (int t = 30; t >= 0; t--) {
      lcd.setCursor(18, 3);
      if (t < 10) {
        lcd.print(" ");
      }
      lcd.print(t);
      delay(1000);
    }
  } else {
    lcd.clear();
    showText("Väärin meni.");
    lcd.setCursor(0,1);
    showText("Yritä uudelleen.");
    lcd.setCursor(19,3);
    lcd.write(right);
    while (waitJoystick() != 1) {}
  }
}
