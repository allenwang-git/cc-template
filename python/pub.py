from dataclasses import dataclass

from cyclonedds.idl import IdlStruct
import cyclonedds.idl.annotations as annotate


# Define a HelloWorld datatype with one member, data, with as type 'string'
# In IDL this would be defined as "struct HelloWorld { string data; };"
@dataclass
@annotate.final
class HelloWorld(IdlStruct, typename="HelloWorld.Msg"):
    data: str

from cyclonedds.domain import DomainParticipant
from cyclonedds.pub import DataWriter, Publisher
from cyclonedds.topic import Topic
from cyclonedds.core import Policy, Qos
from cyclonedds.util import duration

import time

# Qos seetings
qos = Qos(
    Policy.Reliability.Reliable(duration(microseconds=60)),
    Policy.Deadline(duration(microseconds=10)),
    Policy.Durability.TransientLocal,
    Policy.History.KeepLast(10)
)

# Create a DomainParticipant, your entrypoint to DDS
# Created in the default domain
domain_participant = DomainParticipant(domain_id=11)

# Create a Topic with topic name "Hello" and as datatype "HelloWorld" structs.
topic = Topic(domain_participant, 'Hello', HelloWorld, qos=qos)

# Create a Publisher
publisher = Publisher(domain_participant)

# Create a DataWriter that can send structs on the "Hello" topic
writer = DataWriter(publisher, topic)

for i in range(10):
    Msg = HelloWorld(data=f"Hello World {i+1}")
    writer.write(Msg)
    time.sleep(0.1)
    print(f"Sent Msg {i+1}")