# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: socialhub.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='socialhub.proto',
  package='protobufs.socialhubconnectors',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0fsocialhub.proto\x12\x1dprotobufs.socialhubconnectors\x1a\x1fgoogle/protobuf/timestamp.proto\"\xff\x01\n\x11socialHubResponce\x12\x39\n\x08\x66\x61\x63\x65\x42ook\x18\x01 \x01(\x0b\x32\'.protobufs.socialhubconnectors.FaceBook\x12;\n\tinstagram\x18\x02 \x01(\x0b\x32(.protobufs.socialhubconnectors.Instagram\x12\x37\n\x07twitter\x18\x03 \x01(\x0b\x32&.protobufs.socialhubconnectors.Twitter\x12\x39\n\x08linkedIn\x18\x04 \x01(\x0b\x32\'.protobufs.socialhubconnectors.LinkedIn\"\xfe\x01\n\x10socialHubRequest\x12\x39\n\x08\x66\x61\x63\x65\x42ook\x18\x01 \x01(\x0b\x32\'.protobufs.socialhubconnectors.FaceBook\x12;\n\tinstagram\x18\x02 \x01(\x0b\x32(.protobufs.socialhubconnectors.Instagram\x12\x37\n\x07twitter\x18\x03 \x01(\x0b\x32&.protobufs.socialhubconnectors.Twitter\x12\x39\n\x08linkedIn\x18\x04 \x01(\x0b\x32\'.protobufs.socialhubconnectors.LinkedIn\">\n\x08\x46\x61\x63\x65\x42ook\x12\r\n\x05\x61ppId\x18\x01 \x01(\t\x12\x13\n\x0b\x61\x63\x63\x65ssToken\x18\x02 \x01(\t\x12\x0e\n\x06Object\x18\x03 \x01(\t\"?\n\tInstagram\x12\r\n\x05\x61ppId\x18\x01 \x01(\t\x12\x13\n\x0b\x61\x63\x63\x65ssToken\x18\x02 \x01(\t\x12\x0e\n\x06Object\x18\x03 \x01(\t\"=\n\x07Twitter\x12\r\n\x05\x61ppId\x18\x01 \x01(\t\x12\x13\n\x0b\x61\x63\x63\x65ssToken\x18\x02 \x01(\t\x12\x0e\n\x06Object\x18\x03 \x01(\t\">\n\x08LinkedIn\x12\r\n\x05\x61ppId\x18\x01 \x01(\t\x12\x13\n\x0b\x61\x63\x63\x65ssToken\x18\x02 \x01(\t\x12\x0e\n\x06Object\x18\x03 \x01(\t2\xfe\x01\n\x13socialHubConnectors\x12r\n\x0bgetUserData\x12/.protobufs.socialhubconnectors.socialHubRequest\x1a\x30.protobufs.socialhubconnectors.socialHubResponce\"\x00\x12s\n\x0cpostUserData\x12/.protobufs.socialhubconnectors.socialHubRequest\x1a\x30.protobufs.socialhubconnectors.socialHubResponce\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_SOCIALHUBRESPONCE = _descriptor.Descriptor(
  name='socialHubResponce',
  full_name='protobufs.socialhubconnectors.socialHubResponce',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='faceBook', full_name='protobufs.socialhubconnectors.socialHubResponce.faceBook', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instagram', full_name='protobufs.socialhubconnectors.socialHubResponce.instagram', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='twitter', full_name='protobufs.socialhubconnectors.socialHubResponce.twitter', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='linkedIn', full_name='protobufs.socialhubconnectors.socialHubResponce.linkedIn', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=84,
  serialized_end=339,
)


_SOCIALHUBREQUEST = _descriptor.Descriptor(
  name='socialHubRequest',
  full_name='protobufs.socialhubconnectors.socialHubRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='faceBook', full_name='protobufs.socialhubconnectors.socialHubRequest.faceBook', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instagram', full_name='protobufs.socialhubconnectors.socialHubRequest.instagram', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='twitter', full_name='protobufs.socialhubconnectors.socialHubRequest.twitter', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='linkedIn', full_name='protobufs.socialhubconnectors.socialHubRequest.linkedIn', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=342,
  serialized_end=596,
)


_FACEBOOK = _descriptor.Descriptor(
  name='FaceBook',
  full_name='protobufs.socialhubconnectors.FaceBook',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='appId', full_name='protobufs.socialhubconnectors.FaceBook.appId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accessToken', full_name='protobufs.socialhubconnectors.FaceBook.accessToken', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Object', full_name='protobufs.socialhubconnectors.FaceBook.Object', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=598,
  serialized_end=660,
)


_INSTAGRAM = _descriptor.Descriptor(
  name='Instagram',
  full_name='protobufs.socialhubconnectors.Instagram',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='appId', full_name='protobufs.socialhubconnectors.Instagram.appId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accessToken', full_name='protobufs.socialhubconnectors.Instagram.accessToken', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Object', full_name='protobufs.socialhubconnectors.Instagram.Object', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=662,
  serialized_end=725,
)


_TWITTER = _descriptor.Descriptor(
  name='Twitter',
  full_name='protobufs.socialhubconnectors.Twitter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='appId', full_name='protobufs.socialhubconnectors.Twitter.appId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accessToken', full_name='protobufs.socialhubconnectors.Twitter.accessToken', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Object', full_name='protobufs.socialhubconnectors.Twitter.Object', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=727,
  serialized_end=788,
)


_LINKEDIN = _descriptor.Descriptor(
  name='LinkedIn',
  full_name='protobufs.socialhubconnectors.LinkedIn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='appId', full_name='protobufs.socialhubconnectors.LinkedIn.appId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accessToken', full_name='protobufs.socialhubconnectors.LinkedIn.accessToken', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Object', full_name='protobufs.socialhubconnectors.LinkedIn.Object', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=790,
  serialized_end=852,
)

_SOCIALHUBRESPONCE.fields_by_name['faceBook'].message_type = _FACEBOOK
_SOCIALHUBRESPONCE.fields_by_name['instagram'].message_type = _INSTAGRAM
_SOCIALHUBRESPONCE.fields_by_name['twitter'].message_type = _TWITTER
_SOCIALHUBRESPONCE.fields_by_name['linkedIn'].message_type = _LINKEDIN
_SOCIALHUBREQUEST.fields_by_name['faceBook'].message_type = _FACEBOOK
_SOCIALHUBREQUEST.fields_by_name['instagram'].message_type = _INSTAGRAM
_SOCIALHUBREQUEST.fields_by_name['twitter'].message_type = _TWITTER
_SOCIALHUBREQUEST.fields_by_name['linkedIn'].message_type = _LINKEDIN
DESCRIPTOR.message_types_by_name['socialHubResponce'] = _SOCIALHUBRESPONCE
DESCRIPTOR.message_types_by_name['socialHubRequest'] = _SOCIALHUBREQUEST
DESCRIPTOR.message_types_by_name['FaceBook'] = _FACEBOOK
DESCRIPTOR.message_types_by_name['Instagram'] = _INSTAGRAM
DESCRIPTOR.message_types_by_name['Twitter'] = _TWITTER
DESCRIPTOR.message_types_by_name['LinkedIn'] = _LINKEDIN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

socialHubResponce = _reflection.GeneratedProtocolMessageType('socialHubResponce', (_message.Message,), {
  'DESCRIPTOR' : _SOCIALHUBRESPONCE,
  '__module__' : 'socialhub_pb2'
  # @@protoc_insertion_point(class_scope:protobufs.socialhubconnectors.socialHubResponce)
  })
_sym_db.RegisterMessage(socialHubResponce)

socialHubRequest = _reflection.GeneratedProtocolMessageType('socialHubRequest', (_message.Message,), {
  'DESCRIPTOR' : _SOCIALHUBREQUEST,
  '__module__' : 'socialhub_pb2'
  # @@protoc_insertion_point(class_scope:protobufs.socialhubconnectors.socialHubRequest)
  })
_sym_db.RegisterMessage(socialHubRequest)

FaceBook = _reflection.GeneratedProtocolMessageType('FaceBook', (_message.Message,), {
  'DESCRIPTOR' : _FACEBOOK,
  '__module__' : 'socialhub_pb2'
  # @@protoc_insertion_point(class_scope:protobufs.socialhubconnectors.FaceBook)
  })
_sym_db.RegisterMessage(FaceBook)

Instagram = _reflection.GeneratedProtocolMessageType('Instagram', (_message.Message,), {
  'DESCRIPTOR' : _INSTAGRAM,
  '__module__' : 'socialhub_pb2'
  # @@protoc_insertion_point(class_scope:protobufs.socialhubconnectors.Instagram)
  })
_sym_db.RegisterMessage(Instagram)

Twitter = _reflection.GeneratedProtocolMessageType('Twitter', (_message.Message,), {
  'DESCRIPTOR' : _TWITTER,
  '__module__' : 'socialhub_pb2'
  # @@protoc_insertion_point(class_scope:protobufs.socialhubconnectors.Twitter)
  })
_sym_db.RegisterMessage(Twitter)

LinkedIn = _reflection.GeneratedProtocolMessageType('LinkedIn', (_message.Message,), {
  'DESCRIPTOR' : _LINKEDIN,
  '__module__' : 'socialhub_pb2'
  # @@protoc_insertion_point(class_scope:protobufs.socialhubconnectors.LinkedIn)
  })
_sym_db.RegisterMessage(LinkedIn)



_SOCIALHUBCONNECTORS = _descriptor.ServiceDescriptor(
  name='socialHubConnectors',
  full_name='protobufs.socialhubconnectors.socialHubConnectors',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=855,
  serialized_end=1109,
  methods=[
  _descriptor.MethodDescriptor(
    name='getUserData',
    full_name='protobufs.socialhubconnectors.socialHubConnectors.getUserData',
    index=0,
    containing_service=None,
    input_type=_SOCIALHUBREQUEST,
    output_type=_SOCIALHUBRESPONCE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='postUserData',
    full_name='protobufs.socialhubconnectors.socialHubConnectors.postUserData',
    index=1,
    containing_service=None,
    input_type=_SOCIALHUBREQUEST,
    output_type=_SOCIALHUBRESPONCE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SOCIALHUBCONNECTORS)

DESCRIPTOR.services_by_name['socialHubConnectors'] = _SOCIALHUBCONNECTORS

# @@protoc_insertion_point(module_scope)
