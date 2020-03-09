# import torch.nn as nn
# import torch.nn.init as init
# import torch.onnx
# import sys
# from onnx import onnx_pb
# from onnx_coreml import convert

# # con
# model_path = '/data/vibe_data/vibe_model_w_3dpw.pth.tar'




# # convert to core ML 


# model_in = sys.argv[1]
# model_out = sys.argv[2]

# model_file = open(model_in, 'rb')
# model_proto = onnx_pb.ModelProto()
# model_proto.ParseFromString(model_file.read())
# coreml_model = convert(model_proto, image_input_names=['0'], image_output_names=['186'])
# coreml_model.save(model_out)
