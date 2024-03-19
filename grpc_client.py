import grpc
import posts_pb2
import posts_pb2_grpc

# Set the gRPC server address and port
SERVER_ADDRESS = 'localhost:50051'

def check_communication():
    # Create a gRPC channel to connect to the server
    channel = grpc.insecure_channel(SERVER_ADDRESS)

    # Create a stub for the Posts service
    stub = posts_pb2_grpc.PostsStub(channel)

    # Make a remote procedure call (RPC) to get the custom message from the server
    custom_message_request = posts_pb2.CustomMessageRequest()
    response = stub.SendCustomMessage(custom_message_request)

    # Print the custom message received from the server
    print(f"Custom Message: {response.message}")

if __name__ == '__main__':
    check_communication()
