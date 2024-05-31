import multiprocessing.process
import time
import serial
import serial.tools.list_ports
import paho.mqtt.client as paho
from paho import mqtt
import multiprocessing




ports = serial.tools.list_ports.comports()
for p in ports:
    print(p.device)
print(len(ports), 'ports found')




ser = serial.Serial('COM3', 9600)
ser.flushInput()
buf = bytearray(45)


client = paho.Client()
client.connect("localhost", 1883)

# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    """
        Prints the result of the connection with a reasoncode to stdout ( used as callback for connect )

        :param client: the client itself
        :param userdata: userdata is set when initiating the client, here it is userdata=None
        :param flags: these are response flags sent by the broker
        :param rc: stands for reasonCode, which is a code for the connection result
        :param properties: can be used in MQTTv5, but is optional
    """
    print("CONNACK received with code %s." % rc)


# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    """
        Prints mid to stdout to reassure a successful publish ( used as callback for publish )

        :param client: the client itself
        :param userdata: userdata is set when initiating the client, here it is userdata=None
        :param mid: variable returned from the corresponding publish() call, to allow outgoing messages to be tracked
        :param properties: can be used in MQTTv5, but is optional
    """
    print("mid: " + str(mid))


# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    """
        Prints a reassurance for successfully subscribing

        :param client: the client itself
        :param userdata: userdata is set when initiating the client, here it is userdata=None
        :param mid: variable returned from the corresponding publish() call, to allow outgoing messages to be tracked
        :param granted_qos: this is the qos that you declare when subscribing, use the same one for publishing
        :param properties: can be used in MQTTv5, but is optional
    """
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    """
        Prints a mqtt message to stdout ( used as callback for subscribe )

        :param client: the client itself
        :param userdata: userdata is set when initiating the client, here it is userdata=None
        :param msg: the message with topic and payload
    """
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))




client.subscribe("temp/#")
client.subscribe("humidity/#")
client.subscribe("Conductivity/#")
client.subscribe("pH Value/#")
client.subscribe("Nitrogen/#")
client.subscribe("Phosphorus/#")
client.subscribe("Potassium/#")
client.subscribe("Water Level/#")
client.subscribe("temp2/#")
client.subscribe("humidity2/#")
client.subscribe("Conductivity2/#")
client.subscribe("pH Value2/#")
client.subscribe("Nitrogen2/#")
client.subscribe("Phosphorus2/#")
client.subscribe("Potassium2/#")
client.subscribe("temp3/#")
client.subscribe("humidity3/#")
client.subscribe("Conductivity3/#")
client.subscribe("pH Value3/#")
client.subscribe("Nitrogen3/#")
client.subscribe("Phosphorus3/#")
client.subscribe("Potassium3/#")

prepare_to_send=""

client.subscribe("button/1")
def on_message(client, userdata, msg):
    global prepare_to_send
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
    if msg.topic == "button/1" and( msg.payload.decode() == "true"or msg.payload.decode()=="false"):
        print(f"ser.write({msg.payload.decode()})")
        prepare_to_send=str.encode((msg.payload.decode()),encoding="UTF-8")
    print()
client.on_message=on_message


def main():
    cloop=multiprocessing.Process(target=client_loop,args=(0,))
    sread=multiprocessing.Process(target=serial_read,args=(0,))
    sread.start()
    cloop.start()
    sread.join()
    cloop.join()

def client_loop(a):
    # you can also use loop_start and loop_stop
    client.loop_forever()

def serial_read(a):
    global prepare_to_send
    while (True):

        rx_raw = ser.read(45)  #

        # Convert the hex string to bytes
        payload = rx_raw
        # Decode the payload in Python
        Raw_temperature = (payload[1] << 8) | payload[2]
        temperature = Raw_temperature / 100.0
        if temperature > 100:
            temperature = 100
        Raw_humidity = (payload[3] << 8) | payload[4]
        humidity = Raw_humidity / 100.0
        if humidity > 100:
            humidity = 100
        Raw_conductivity = (payload[5] << 8) | payload[6]
        conductivity = Raw_conductivity / 100.0
        Raw_pHValue = (payload[7] << 8) | payload[8]
        pHValue = Raw_pHValue / 100.0
        if pHValue > 14:
            pHValue = 14
        Raw_nitrogen = (payload[9] << 8) | payload[10]
        nitrogen = Raw_nitrogen / 100.0
        Raw_phosphorus = (payload[11] << 8) | payload[12]
        phosphorus = Raw_phosphorus / 100.0
        Raw_potassium = (payload[13] << 8) | payload[14]
        potassium = Raw_potassium / 100.0
        Raw_waterlevel = (payload[15] << 8) | payload[16]
        waterlevel = Raw_waterlevel
        if waterlevel > 100:
            waterlevel = 100

        Raw_temperature2 = (payload[17] << 8) | payload[18]
        temperature2 = Raw_temperature2 / 100.0
        if temperature2 > 100:
            temperature2 = 100
        Raw_humidity2 = (payload[19] << 8) | payload[20]
        humidity2 = Raw_humidity2 / 100.0
        if humidity2 > 100:
            humidity2 = 100
        Raw_conductivity2 = (payload[21] << 8) | payload[22]
        conductivity2 = Raw_conductivity2 / 100.0
        Raw_pHValue2 = (payload[23] << 8) | payload[24]
        pHValue2 = Raw_pHValue2 / 100.0
        if pHValue2 > 14:
            pHValue2 = 14
        Raw_nitrogen2 = (payload[25] << 8) | payload[26]
        nitrogen2 = Raw_nitrogen2 / 100.0
        Raw_phosphorus2 = (payload[27] << 8) | payload[28]
        phosphorus2 = Raw_phosphorus2 / 100.0
        Raw_potassium2 = (payload[29] << 8) | payload[30]
        potassium2 = Raw_potassium2 / 100.0

        Raw_temperature3 = (payload[31] << 8) | payload[32]
        temperature3 = Raw_temperature3 / 100.0
        if temperature3 > 100:
            temperature3 = 100
        Raw_humidity3 = (payload[33] << 8) | payload[34]
        humidity3 = Raw_humidity3 / 100.0
        if humidity3 > 100:
            humidity3 = 100
        Raw_conductivity3 = (payload[35] << 8) | payload[36]
        conductivity3 = Raw_conductivity3 / 100.0
        Raw_pHValue3 = (payload[37] << 8) | payload[38]
        pHValue3 = Raw_pHValue3 / 100.0
        if pHValue3 > 14:
            pHValue3 = 14
        Raw_nitrogen3 = (payload[39] << 8) | payload[40]
        nitrogen3 = Raw_nitrogen3 / 100.0
        Raw_phosphorus3 = (payload[41] << 8) | payload[42]
        phosphorus3 = Raw_phosphorus3 / 100.0
        Raw_potassium3 = (payload[43] << 8) | payload[44]
        potassium3 = Raw_potassium3 / 100.0

        # a single publish, this can also be done in loops, etc.
        client.publish("temp", payload=temperature)
        client.publish("humidity", payload=humidity)
        client.publish("Conductivity", payload=conductivity)
        client.publish("pH Value", payload=pHValue)
        client.publish("Nitrogen", payload=nitrogen)
        client.publish("Phosphorus", payload=phosphorus)
        client.publish("Potassium", payload=potassium)
        client.publish("Water Level", payload=waterlevel)

        client.publish("temp2", payload=temperature2)
        client.publish("humidity2", payload=humidity2)
        client.publish("Conductivity2", payload=conductivity2)
        client.publish("pH Value2", payload=pHValue2)
        client.publish("Nitrogen2", payload=nitrogen2)
        client.publish("Phosphorus2", payload=phosphorus2)
        client.publish("Potassium2", payload=potassium2)

        client.publish("temp3", payload=temperature3)
        client.publish("humidity3", payload=humidity3)
        client.publish("Conductivity3", payload=conductivity3)
        client.publish("pH Value3", payload=pHValue3)
        client.publish("Nitrogen3", payload=nitrogen3)
        client.publish("Phosphorus3", payload=phosphorus3)
        client.publish("Potassium3", payload=potassium3)
        ser.write(prepare_to_send)



if __name__ == "__main__":
    main()