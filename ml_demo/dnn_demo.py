import tensorflow as tf
import numpy as np

# 开启 Eager Execution 模式
# tf.enable_eager_execution() # TensorFlow 2.x 将默认使用Eager Execution模式

# 模型参数
input_size = 1
hidden_size = 64
num_layers = 2
output_size = 1

# 生成虚拟数据
data = np.random.rand(100, 10, input_size).astype(np.float32)
labels = np.random.rand(100, output_size).astype(np.float32)

# 使用 tf.data 来加载数据
dataset = tf.data.Dataset.from_tensor_slices((data, labels))
dataset = dataset.shuffle(buffer_size=100).batch(10)

# 创建深度循环神经网络
model = tf.keras.Sequential()
for _ in range(num_layers): # 循环层num_layers个数
    model.add(tf.keras.layers.SimpleRNN(hidden_size, return_sequences=True))
model.add(tf.keras.layers.SimpleRNN(hidden_size))
model.add(tf.keras.layers.Dense(output_size))

# 定义损失函数和优化器
loss_fn = tf.keras.losses.MeanSquaredError()
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)

# 训练模型
for epoch in range(10):
    for batch_data, batch_labels in dataset:
        with tf.GradientTape() as tape:
            predictions = model(batch_data)
            loss = loss_fn(batch_labels, predictions)
        gradients = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(gradients, model.trainable_variables))
    
    print(f'Epoch {epoch + 1}, Loss: {loss.numpy()}')

# 模型训练完成，可以进行预测


"""

下面是一个简单的使用TensorFlow的DRNN示例：
在较新版本的TensorFlow中，使用tf.placeholder来定义占位符已经被弃用。
你应该使用tf.compat.v1.placeholder来定义占位符，
或者更好的方法是使用tf.data API来加载和处理数据

如果你使用的是TensorFlow 2.x，建议使用更现代的方法，如tf.data API来加载和处理数据，
因为tf.placeholder和静态图（Graph）已经被
Eager Execution和动态图（Dynamic Graph）所取代。


# 在这里，你可以准备数据和进行模型训练
这个示例使用TensorFlow构建了一个深层循环神经网络，其中包括两个循环层（num_layers=2），
输入维度为1，隐藏状态维度为64，输出维度为1。你可以根据你的需求和数据进行相应的调整。

这个示例中，我们使用了 tf.nn.rnn_cell.MultiRNNCell 来创建多层循环神经网络，
并使用 tf.nn.dynamic_rnn 来执行前向传播。然后，我们添加了一个输出层，
定义了损失函数和优化器，以进行模型训练。

记得在实际应用中，你需要适应你的任务需求、数据处理、训练循环等等。
TensorFlow提供了广泛的工具和函数，可以帮助你实现和训练深度循环神经网络。"""
