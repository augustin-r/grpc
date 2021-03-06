# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test/cpp/interop/test.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from test.cpp.interop import empty_pb2 as test_dot_cpp_dot_interop_dot_empty__pb2
from test.cpp.interop import messages_pb2 as test_dot_cpp_dot_interop_dot_messages__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='test/cpp/interop/test.proto',
  package='grpc.testing',
  serialized_pb=_b('\n\x1btest/cpp/interop/test.proto\x12\x0cgrpc.testing\x1a\x1ctest/cpp/interop/empty.proto\x1a\x1ftest/cpp/interop/messages.proto2\xbb\x04\n\x0bTestService\x12\x35\n\tEmptyCall\x12\x13.grpc.testing.Empty\x1a\x13.grpc.testing.Empty\x12\x46\n\tUnaryCall\x12\x1b.grpc.testing.SimpleRequest\x1a\x1c.grpc.testing.SimpleResponse\x12l\n\x13StreamingOutputCall\x12(.grpc.testing.StreamingOutputCallRequest\x1a).grpc.testing.StreamingOutputCallResponse0\x01\x12i\n\x12StreamingInputCall\x12\'.grpc.testing.StreamingInputCallRequest\x1a(.grpc.testing.StreamingInputCallResponse(\x01\x12i\n\x0e\x46ullDuplexCall\x12(.grpc.testing.StreamingOutputCallRequest\x1a).grpc.testing.StreamingOutputCallResponse(\x01\x30\x01\x12i\n\x0eHalfDuplexCall\x12(.grpc.testing.StreamingOutputCallRequest\x1a).grpc.testing.StreamingOutputCallResponse(\x01\x30\x01')
  ,
  dependencies=[test_dot_cpp_dot_interop_dot_empty__pb2.DESCRIPTOR,test_dot_cpp_dot_interop_dot_messages__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)





import abc
from grpc.early_adopter import implementations
from grpc.framework.alpha import utilities
class EarlyAdopterTestServiceServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def EmptyCall(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def UnaryCall(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def StreamingOutputCall(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def StreamingInputCall(self, request_iterator, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def FullDuplexCall(self, request_iterator, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def HalfDuplexCall(self, request_iterator, context):
    raise NotImplementedError()
class EarlyAdopterTestServiceServer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def start(self):
    raise NotImplementedError()
  @abc.abstractmethod
  def stop(self):
    raise NotImplementedError()
class EarlyAdopterTestServiceStub(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def EmptyCall(self, request):
    raise NotImplementedError()
  EmptyCall.async = None
  @abc.abstractmethod
  def UnaryCall(self, request):
    raise NotImplementedError()
  UnaryCall.async = None
  @abc.abstractmethod
  def StreamingOutputCall(self, request):
    raise NotImplementedError()
  StreamingOutputCall.async = None
  @abc.abstractmethod
  def StreamingInputCall(self, request_iterator):
    raise NotImplementedError()
  StreamingInputCall.async = None
  @abc.abstractmethod
  def FullDuplexCall(self, request_iterator):
    raise NotImplementedError()
  FullDuplexCall.async = None
  @abc.abstractmethod
  def HalfDuplexCall(self, request_iterator):
    raise NotImplementedError()
  HalfDuplexCall.async = None
def early_adopter_create_TestService_server(servicer, port, private_key=None, certificate_chain=None):
  import test.cpp.interop.empty_pb2
  import test.cpp.interop.empty_pb2
  import test.cpp.interop.messages_pb2
  import test.cpp.interop.messages_pb2
  import test.cpp.interop.messages_pb2
  import test.cpp.interop.messages_pb2
  import test.cpp.interop.messages_pb2
  import test.cpp.interop.messages_pb2
  import test.cpp.interop.messages_pb2
  import test.cpp.interop.messages_pb2
  import test.cpp.interop.messages_pb2
  import test.cpp.interop.messages_pb2
  method_service_descriptions = {
    "EmptyCall": utilities.unary_unary_service_description(
      servicer.EmptyCall,
      test.cpp.interop.empty_pb2.Empty.FromString,
      test.cpp.interop.empty_pb2.Empty.SerializeToString,
    ),
    "FullDuplexCall": utilities.stream_stream_service_description(
      servicer.FullDuplexCall,
      test.cpp.interop.messages_pb2.StreamingOutputCallRequest.FromString,
      test.cpp.interop.messages_pb2.StreamingOutputCallResponse.SerializeToString,
    ),
    "HalfDuplexCall": utilities.stream_stream_service_description(
      servicer.HalfDuplexCall,
      test.cpp.interop.messages_pb2.StreamingOutputCallRequest.FromString,
      test.cpp.interop.messages_pb2.StreamingOutputCallResponse.SerializeToString,
    ),
    "StreamingInputCall": utilities.stream_unary_service_description(
      servicer.StreamingInputCall,
      test.cpp.interop.messages_pb2.StreamingInputCallRequest.FromString,
      test.cpp.interop.messages_pb2.StreamingInputCallResponse.SerializeToString,
    ),
    "StreamingOutputCall": utilities.unary_stream_service_description(
      servicer.StreamingOutputCall,
      test.cpp.interop.messages_pb2.StreamingOutputCallRequest.FromString,
      test.cpp.interop.messages_pb2.StreamingOutputCallResponse.SerializeToString,
    ),
    "UnaryCall": utilities.unary_unary_service_description(
      servicer.UnaryCall,
      test.cpp.interop.messages_pb2.SimpleRequest.FromString,
      test.cpp.interop.messages_pb2.SimpleResponse.SerializeToString,
    ),
  }
  return implementations.server("grpc.testing.TestService", method_service_descriptions, port, private_key=private_key, certificate_chain=certificate_chain)
def early_adopter_create_TestService_stub(host, port, metadata_transformer=None, secure=False, root_certificates=None, private_key=None, certificate_chain=None, server_host_override=None):
  import test.cpp.interop.empty_pb2
  import test.cpp.interop.empty_pb2
  import test.cpp.interop.messages_pb2
  import test.cpp.interop.messages_pb2
  import test.cpp.interop.messages_pb2
  import test.cpp.interop.messages_pb2
  import test.cpp.interop.messages_pb2
  import test.cpp.interop.messages_pb2
  import test.cpp.interop.messages_pb2
  import test.cpp.interop.messages_pb2
  import test.cpp.interop.messages_pb2
  import test.cpp.interop.messages_pb2
  method_invocation_descriptions = {
    "EmptyCall": utilities.unary_unary_invocation_description(
      test.cpp.interop.empty_pb2.Empty.SerializeToString,
      test.cpp.interop.empty_pb2.Empty.FromString,
    ),
    "FullDuplexCall": utilities.stream_stream_invocation_description(
      test.cpp.interop.messages_pb2.StreamingOutputCallRequest.SerializeToString,
      test.cpp.interop.messages_pb2.StreamingOutputCallResponse.FromString,
    ),
    "HalfDuplexCall": utilities.stream_stream_invocation_description(
      test.cpp.interop.messages_pb2.StreamingOutputCallRequest.SerializeToString,
      test.cpp.interop.messages_pb2.StreamingOutputCallResponse.FromString,
    ),
    "StreamingInputCall": utilities.stream_unary_invocation_description(
      test.cpp.interop.messages_pb2.StreamingInputCallRequest.SerializeToString,
      test.cpp.interop.messages_pb2.StreamingInputCallResponse.FromString,
    ),
    "StreamingOutputCall": utilities.unary_stream_invocation_description(
      test.cpp.interop.messages_pb2.StreamingOutputCallRequest.SerializeToString,
      test.cpp.interop.messages_pb2.StreamingOutputCallResponse.FromString,
    ),
    "UnaryCall": utilities.unary_unary_invocation_description(
      test.cpp.interop.messages_pb2.SimpleRequest.SerializeToString,
      test.cpp.interop.messages_pb2.SimpleResponse.FromString,
    ),
  }
  return implementations.stub("grpc.testing.TestService", method_invocation_descriptions, host, port, metadata_transformer=metadata_transformer, secure=secure, root_certificates=root_certificates, private_key=private_key, certificate_chain=certificate_chain, server_host_override=server_host_override)
# @@protoc_insertion_point(module_scope)
