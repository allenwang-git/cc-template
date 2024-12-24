from dataclasses import dataclass

from cyclonedds.idl import IdlStruct
import cyclonedds.idl.annotations as annotate


# Define a HelloWorld datatype with one member, data, with as type 'string'
# In IDL this would be defined as "struct HelloWorld { string data; };"
@dataclass
@annotate.final
class HelloWorld(IdlStruct, typename="HelloWorld.Msg"):
    data: str


from cyclonedds.core import  Qos, Policy
from cyclonedds.domain import DomainParticipant
from cyclonedds.topic import Topic
from cyclonedds.sub import Subscriber, DataReader
from cyclonedds.util import duration


qos = Qos(
    Policy.Reliability.Reliable(duration(microseconds=60)),
    Policy.Deadline(duration(microseconds=10)),
    Policy.Durability.TransientLocal,
    Policy.History.KeepLast(10)
)

domain_participant = DomainParticipant(domain_id=11)
topic = Topic(domain_participant, 'Hello', HelloWorld, qos=qos)
subscriber = Subscriber(domain_participant)
reader = DataReader(domain_participant, topic)

received_num = 0
for sample in reader.take_iter(timeout=duration(seconds=5)):
    print(f"received msg {sample.data}")
    received_num += 1
    if received_num == 10:
        print("All msg received.")