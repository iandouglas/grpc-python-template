# grpc-python

Compile protos

```bash
python -m grpc_tools.protoc -I protobufs --python_out=src/ --grpc_python_out=src/ protobufs/definition.proto
```

Requires PostgreSQL to be running with a 'postgres' role by default.
