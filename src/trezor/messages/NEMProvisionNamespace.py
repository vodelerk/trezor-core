# Automatically generated by pb2py
import protobuf as p


class NEMProvisionNamespace(p.MessageType):
    FIELDS = {
        1: ('namespace', p.UnicodeType, 0),
        2: ('parent', p.UnicodeType, 0),
        3: ('sink', p.UnicodeType, 0),
        4: ('fee', p.UVarintType, 0),
    }
