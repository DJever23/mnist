import input_data
mnist=input_data.read_data_sets('Mnist_data',one_hot=True)
print('训练数据集的大小为:%d'%(mnist.train.num_examples))
print('测试数据集的大小为:%d'%(mnist.test.num_examples))
