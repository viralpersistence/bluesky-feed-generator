from server import config
from server import data_stream
from server.data_filter import operations_callback

if __name__ == '__main__':
    data_stream.run(config.SERVICE_DID, operations_callback)