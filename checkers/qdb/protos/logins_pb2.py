# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/logins.proto

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
  name='protos/logins.proto',
  package='crypto',
  serialized_pb=_b('\n\x13protos/logins.proto\x12\x06\x63rypto\x1a\x12protos/utils.proto\"\x16\n\x06Logins\x12\x0c\n\x04name\x18\x01 \x03(\x0c:.\n\x06LOGINS\x12\x0e.crypto.Option\x18\n \x01(\x0b\x32\x0e.crypto.Logins')
  ,
  dependencies=[protos.utils_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


LOGINS_FIELD_NUMBER = 10
LOGINS = _descriptor.FieldDescriptor(
  name='LOGINS', full_name='crypto.LOGINS', index=0,
  number=10, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_LOGINS = _descriptor.Descriptor(
  name='Logins',
  full_name='crypto.Logins',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='crypto.Logins.name', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=51,
  serialized_end=73,
)

DESCRIPTOR.message_types_by_name['Logins'] = _LOGINS
DESCRIPTOR.extensions_by_name['LOGINS'] = LOGINS

Logins = _reflection.GeneratedProtocolMessageType('Logins', (_message.Message,), dict(
  DESCRIPTOR = _LOGINS,
  __module__ = 'protos.logins_pb2'
  # @@protoc_insertion_point(class_scope:crypto.Logins)
  ))
_sym_db.RegisterMessage(Logins)

LOGINS.message_type = _LOGINS
protos.utils_pb2.Option.RegisterExtension(LOGINS)

# @@protoc_insertion_point(module_scope)
