.PHONY: proto

proto:
	python -m grpc_tools.protoc -I./$(DIR) --python_out=$(DIR) --pyi_out=$(DIR) --grpc_python_out=$(DIR) $(DIR)/*.proto