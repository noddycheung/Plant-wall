import multiprocessing.process
import time
import serial
import serial.tools.list_ports
import paho.mqtt.client as paho
from paho import mqtt

client = paho.Client()
client.connect("localhost", 1883)
data = [""]
data[0] = "false"
with open('panel_data.txt', 'w', encoding='utf-8') as file: 
            file.writelines(data) 
            file.close()

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

client.subscribe("button/1")
def on_message(client, userdata, msg):
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
    if msg.topic == "button/1" and( msg.payload.decode() == "true"or msg.payload.decode()=="false"):
        print(f"ser.write({msg.payload.decode()})")
        
        # with open('panel_data.txt', 'r', encoding='utf-8') as file: 
        data = [""]
        data[0] = msg.payload.decode()
        
        with open('panel_data.txt', 'w', encoding='utf-8') as file: 
            file.writelines(data) 
            file.close()
        
    print()
client.on_message=on_message


def main():
    client_loop()

def client_loop():
    # you can also use loop_start and loop_stop
    client.loop_forever()


if __name__ == "__main__":
    main()