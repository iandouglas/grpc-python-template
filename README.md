# grpc-python

Compile protos

```bash
python -m grpc_tools.protoc -I protobufs --python_out=src/adapters/pb2 --grpc_python_out=src/adapters/pb2 protobufs/definition.proto
```
