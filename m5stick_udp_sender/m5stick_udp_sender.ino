#include <WiFi.h>
#include <WiFiUdp.h>


// 接続先のSSIDとパスワード
const char ssid[] = "aterm-841cf0-g";
const char key[] = "280c505986579";

static WiFiUDP wifiUdp;
static const char *dstIPAddress = "192.168.10.7";//受信側IPアドレス
static const int srcPort = 11110;//送信側ポート
static const int dstPort = 11111;//受信側ポート

//char  replyPacket[] = "Hi there! Got the message :-)";
char  replyPacket[] = "13.3";

const uint8_t aaa = 100;
size_t buff_size = 10;


void WifiSetup() {
  Serial.begin(115200);
  WiFi.begin(ssid, key);
  while ( WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
  wifiUdp.begin(srcPort);
}

void setup() {
  WifiSetup();
  Serial.print("WiFi connected\r\nIP address: ");
  Serial.println(WiFi.localIP());
}
void loop() {
  int i = 0;
  wifiUdp.beginPacket(dstIPAddress, dstPort);
//  while (replyPacket[i] != 0) {
//    wifiUdp.write((uint8_t)replyPacket[i]);
//    i++;
//  }
  wifiUdp.print(replyPacket);
//  wifiUdp.write('a');
  wifiUdp.endPacket();
  Serial.println("Now write!");
  delay(3000);
}
