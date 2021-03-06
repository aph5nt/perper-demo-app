# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fabric.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fabric.proto',
  package='perper',
  syntax='proto3',
  serialized_options=b'\n\032com.obecto.perper.protobufP\001\252\002\030Perper.Protocol.Protobuf',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0c\x66\x61\x62ric.proto\x12\x06perper\x1a\x1bgoogle/protobuf/empty.proto\"I\n\x11\x45xecutionsRequest\x12\r\n\x05\x61gent\x18\x01 \x01(\t\x12\x10\n\x08instance\x18\x02 \x01(\t\x12\x13\n\x0blocalToData\x18\x04 \x01(\x08\"^\n\x12\x45xecutionsResponse\x12\x10\n\x08instance\x18\x02 \x01(\t\x12\x10\n\x08\x64\x65legate\x18\x03 \x01(\t\x12\x11\n\texecution\x18\x04 \x01(\t\x12\x11\n\tcancelled\x18\x05 \x01(\x08\"-\n\x18\x45xecutionFinishedRequest\x12\x11\n\texecution\x18\x04 \x01(\t\"[\n\x12StreamItemsRequest\x12\x0e\n\x06stream\x18\x01 \x01(\t\x12\x10\n\x08startKey\x18\x02 \x01(\x03\x12\x13\n\x0blocalToData\x18\x03 \x01(\x08\x12\x0e\n\x06stride\x18\x04 \x01(\x03\"\"\n\x13StreamItemsResponse\x12\x0b\n\x03key\x18\x01 \x01(\x03\")\n\x17ListenerAttachedRequest\x12\x0e\n\x06stream\x18\x01 \x01(\t2\xbd\x02\n\x06\x46\x61\x62ric\x12G\n\nExecutions\x12\x19.perper.ExecutionsRequest\x1a\x1a.perper.ExecutionsResponse\"\x00\x30\x01\x12O\n\x11\x45xecutionFinished\x12 .perper.ExecutionFinishedRequest\x1a\x16.google.protobuf.Empty\"\x00\x12J\n\x0bStreamItems\x12\x1a.perper.StreamItemsRequest\x1a\x1b.perper.StreamItemsResponse\"\x00\x30\x01\x12M\n\x10ListenerAttached\x12\x1f.perper.ListenerAttachedRequest\x1a\x16.google.protobuf.Empty\"\x00\x42\x39\n\x1a\x63om.obecto.perper.protobufP\x01\xaa\x02\x18Perper.Protocol.Protobufb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_EXECUTIONSREQUEST = _descriptor.Descriptor(
  name='ExecutionsRequest',
  full_name='perper.ExecutionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent', full_name='perper.ExecutionsRequest.agent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instance', full_name='perper.ExecutionsRequest.instance', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='localToData', full_name='perper.ExecutionsRequest.localToData', index=2,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=126,
)


_EXECUTIONSRESPONSE = _descriptor.Descriptor(
  name='ExecutionsResponse',
  full_name='perper.ExecutionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='perper.ExecutionsResponse.instance', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delegate', full_name='perper.ExecutionsResponse.delegate', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='execution', full_name='perper.ExecutionsResponse.execution', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cancelled', full_name='perper.ExecutionsResponse.cancelled', index=3,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=222,
)


_EXECUTIONFINISHEDREQUEST = _descriptor.Descriptor(
  name='ExecutionFinishedRequest',
  full_name='perper.ExecutionFinishedRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='execution', full_name='perper.ExecutionFinishedRequest.execution', index=0,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=224,
  serialized_end=269,
)


_STREAMITEMSREQUEST = _descriptor.Descriptor(
  name='StreamItemsRequest',
  full_name='perper.StreamItemsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='stream', full_name='perper.StreamItemsRequest.stream', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='startKey', full_name='perper.StreamItemsRequest.startKey', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='localToData', full_name='perper.StreamItemsRequest.localToData', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stride', full_name='perper.StreamItemsRequest.stride', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=271,
  serialized_end=362,
)


_STREAMITEMSRESPONSE = _descriptor.Descriptor(
  name='StreamItemsResponse',
  full_name='perper.StreamItemsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='perper.StreamItemsResponse.key', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=364,
  serialized_end=398,
)


_LISTENERATTACHEDREQUEST = _descriptor.Descriptor(
  name='ListenerAttachedRequest',
  full_name='perper.ListenerAttachedRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='stream', full_name='perper.ListenerAttachedRequest.stream', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=400,
  serialized_end=441,
)

DESCRIPTOR.message_types_by_name['ExecutionsRequest'] = _EXECUTIONSREQUEST
DESCRIPTOR.message_types_by_name['ExecutionsResponse'] = _EXECUTIONSRESPONSE
DESCRIPTOR.message_types_by_name['ExecutionFinishedRequest'] = _EXECUTIONFINISHEDREQUEST
DESCRIPTOR.message_types_by_name['StreamItemsRequest'] = _STREAMITEMSREQUEST
DESCRIPTOR.message_types_by_name['StreamItemsResponse'] = _STREAMITEMSRESPONSE
DESCRIPTOR.message_types_by_name['ListenerAttachedRequest'] = _LISTENERATTACHEDREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExecutionsRequest = _reflection.GeneratedProtocolMessageType('ExecutionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTIONSREQUEST,
  '__module__' : 'fabric_pb2'
  # @@protoc_insertion_point(class_scope:perper.ExecutionsRequest)
  })
_sym_db.RegisterMessage(ExecutionsRequest)

ExecutionsResponse = _reflection.GeneratedProtocolMessageType('ExecutionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTIONSRESPONSE,
  '__module__' : 'fabric_pb2'
  # @@protoc_insertion_point(class_scope:perper.ExecutionsResponse)
  })
_sym_db.RegisterMessage(ExecutionsResponse)

ExecutionFinishedRequest = _reflection.GeneratedProtocolMessageType('ExecutionFinishedRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTIONFINISHEDREQUEST,
  '__module__' : 'fabric_pb2'
  # @@protoc_insertion_point(class_scope:perper.ExecutionFinishedRequest)
  })
_sym_db.RegisterMessage(ExecutionFinishedRequest)

StreamItemsRequest = _reflection.GeneratedProtocolMessageType('StreamItemsRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMITEMSREQUEST,
  '__module__' : 'fabric_pb2'
  # @@protoc_insertion_point(class_scope:perper.StreamItemsRequest)
  })
_sym_db.RegisterMessage(StreamItemsRequest)

StreamItemsResponse = _reflection.GeneratedProtocolMessageType('StreamItemsResponse', (_message.Message,), {
  'DESCRIPTOR' : _STREAMITEMSRESPONSE,
  '__module__' : 'fabric_pb2'
  # @@protoc_insertion_point(class_scope:perper.StreamItemsResponse)
  })
_sym_db.RegisterMessage(StreamItemsResponse)

ListenerAttachedRequest = _reflection.GeneratedProtocolMessageType('ListenerAttachedRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTENERATTACHEDREQUEST,
  '__module__' : 'fabric_pb2'
  # @@protoc_insertion_point(class_scope:perper.ListenerAttachedRequest)
  })
_sym_db.RegisterMessage(ListenerAttachedRequest)


DESCRIPTOR._options = None

_FABRIC = _descriptor.ServiceDescriptor(
  name='Fabric',
  full_name='perper.Fabric',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=444,
  serialized_end=761,
  methods=[
  _descriptor.MethodDescriptor(
    name='Executions',
    full_name='perper.Fabric.Executions',
    index=0,
    containing_service=None,
    input_type=_EXECUTIONSREQUEST,
    output_type=_EXECUTIONSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ExecutionFinished',
    full_name='perper.Fabric.ExecutionFinished',
    index=1,
    containing_service=None,
    input_type=_EXECUTIONFINISHEDREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamItems',
    full_name='perper.Fabric.StreamItems',
    index=2,
    containing_service=None,
    input_type=_STREAMITEMSREQUEST,
    output_type=_STREAMITEMSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListenerAttached',
    full_name='perper.Fabric.ListenerAttached',
    index=3,
    containing_service=None,
    input_type=_LISTENERATTACHEDREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FABRIC)

DESCRIPTOR.services_by_name['Fabric'] = _FABRIC

# @@protoc_insertion_point(module_scope)
