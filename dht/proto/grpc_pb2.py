# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: grpc.proto
# Protobuf Python Version: 5.28.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    3,
    '',
    'grpc.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ngrpc.proto\"/\n\x0bTensorEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x13\n\x0btensor_data\x18\x02 \x01(\x0c\"4\n\x13IntermediateTensors\x12\x1d\n\x07tensors\x18\x01 \x03(\x0b\x32\x0c.TensorEntry\"{\n\x0fGrpcRequestData\x12\x1d\n\x15\x65xecute_model_request\x18\x01 \x01(\x0c\x12\x32\n\x14intermediate_tensors\x18\x02 \x01(\x0b\x32\x14.IntermediateTensors\x12\x15\n\rgrpc_metadata\x18\x03 \x01(\x0c\"$\n\rSamplerOutput\x12\x13\n\x0boutput_data\x18\x01 \x01(\x0c\"4\n\x10GrpcResponseData\x12 \n\x08res_data\x18\x01 \x03(\x0b\x32\x0e.SamplerOutputb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TENSORENTRY']._serialized_start=14
  _globals['_TENSORENTRY']._serialized_end=61
  _globals['_INTERMEDIATETENSORS']._serialized_start=63
  _globals['_INTERMEDIATETENSORS']._serialized_end=115
  _globals['_GRPCREQUESTDATA']._serialized_start=117
  _globals['_GRPCREQUESTDATA']._serialized_end=240
  _globals['_SAMPLEROUTPUT']._serialized_start=242
  _globals['_SAMPLEROUTPUT']._serialized_end=278
  _globals['_GRPCRESPONSEDATA']._serialized_start=280
  _globals['_GRPCRESPONSEDATA']._serialized_end=332
# @@protoc_insertion_point(module_scope)
