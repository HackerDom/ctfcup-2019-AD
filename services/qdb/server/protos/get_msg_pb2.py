# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/get_msg.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import protos.utils_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/get_msg.proto',
  package='crypto',
  serialized_pb=_b('\n\x14protos/get_msg.proto\x12\x06\x63rypto\x1a\x12protos/utils.proto\"\x1e\n\rGetMsgRequest\x12\r\n\x05login\x18\x01 \x02(\x0c\"\x1d\n\x0eGetMsgResponse\x12\x0b\n\x03msg\x18\x01 \x02(\x0c:>\n\x0fGET_MSG_REQUEST\x12\x0e.crypto.Option\x18\r \x01(\x0b\x32\x15.crypto.GetMsgRequest:@\n\x10GET_MSG_RESPONSE\x12\x0e.crypto.Option\x18\x0e \x01(\x0b\x32\x16.crypto.GetMsgResponse')
  ,
  dependencies=[protos.utils_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


GET_MSG_REQUEST_FIELD_NUMBER = 13
GET_MSG_REQUEST = _descriptor.FieldDescriptor(
  name='GET_MSG_REQUEST', full_name='crypto.GET_MSG_REQUEST', index=0,
  number=13, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
GET_MSG_RESPONSE_FIELD_NUMBER = 14
GET_MSG_RESPONSE = _descriptor.FieldDescriptor(
  name='GET_MSG_RESPONSE', full_name='crypto.GET_MSG_RESPONSE', index=1,
  number=14, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_GETMSGREQUEST = _descriptor.Descriptor(
  name='GetMsgRequest',
  full_name='crypto.GetMsgRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='login', full_name='crypto.GetMsgRequest.login', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=82,
)


_GETMSGRESPONSE = _descriptor.Descriptor(
  name='GetMsgResponse',
  full_name='crypto.GetMsgResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='crypto.GetMsgResponse.msg', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=113,
)

DESCRIPTOR.message_types_by_name['GetMsgRequest'] = _GETMSGREQUEST
DESCRIPTOR.message_types_by_name['GetMsgResponse'] = _GETMSGRESPONSE
DESCRIPTOR.extensions_by_name['GET_MSG_REQUEST'] = GET_MSG_REQUEST
DESCRIPTOR.extensions_by_name['GET_MSG_RESPONSE'] = GET_MSG_RESPONSE

GetMsgRequest = _reflection.GeneratedProtocolMessageType('GetMsgRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETMSGREQUEST,
  __module__ = 'protos.get_msg_pb2'
  # @@protoc_insertion_point(class_scope:crypto.GetMsgRequest)
  ))
_sym_db.RegisterMessage(GetMsgRequest)

GetMsgResponse = _reflection.GeneratedProtocolMessageType('GetMsgResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETMSGRESPONSE,
  __module__ = 'protos.get_msg_pb2'
  # @@protoc_insertion_point(class_scope:crypto.GetMsgResponse)
  ))
_sym_db.RegisterMessage(GetMsgResponse)

GET_MSG_REQUEST.message_type = _GETMSGREQUEST
protos.utils_pb2.Option.RegisterExtension(GET_MSG_REQUEST)
GET_MSG_RESPONSE.message_type = _GETMSGRESPONSE
protos.utils_pb2.Option.RegisterExtension(GET_MSG_RESPONSE)

# @@protoc_insertion_point(module_scope)
