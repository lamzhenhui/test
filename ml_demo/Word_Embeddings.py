import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

embedding_dim = 1000
max_sequence_length = 1000
batch_size =1000
num_epochs = 100




# 步骤1: 数据准备
corpus = [
    'This is a positive sentence.',
    'Another example of a positive one.',
    'This sentence is negative.',
    'Example of a negative sentence.',
    'i usually play game'
]

tokenizer = Tokenizer()
tokenizer.fit_on_texts(corpus)
total_words = len(tokenizer.word_index) + 1  # +1 是因为索引从1开始

# 步骤2: 构建模型
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(
        input_dim=total_words, output_dim=embedding_dim, input_length=max_sequence_length),
    tf.keras.layers.Flatten(),  # 或使用 GlobalAveragePooling1D
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# 编译模型
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 打印模型概况
model.summary()

# 步骤3: 加载和处理数据
sequences = tokenizer.texts_to_sequences(corpus)
# print(sequences)


padded_sequences = pad_sequences(sequences, maxlen=max_sequence_length, padding='post')
# print(padded_sequences)

labels = [1, 1, 0, 0,1]  # 1 表示 positive，0 表示 negative

# 创建 tf.data 数据集
dataset = tf.data.Dataset.from_tensor_slices((padded_sequences, labels))

dataset = dataset.shuffle(buffer_size=len(corpus)).batch(batch_size)


# 训练模型
model.fit(dataset, epochs=num_epochs)


# 假设这是要进行情绪预测的新句子
new_sentences = [
    'This is a new positive sentence.',
    'This sentence seems to be negative.',
    'i  play game',
    ' play game',
    'i usually play with cat',
    'i ',
    'usually ',
    'play ',
    'with ',
    'cat ',
    'new ',
    'ME'
]

# 对新句子进行标记化处理
new_sequences = tokenizer.texts_to_sequences(new_sentences)

# 填充新句子的序列
padded_new_sequences = pad_sequences(new_sequences, maxlen=max_sequence_length, padding='post')

# 使用模型进行情绪预测
predicted_probabilities = model.predict(padded_new_sequences)

# 根据预测的概率值判断情绪
for sentence, prob in zip(new_sentences, predicted_probabilities):
    if prob > 0.5:
        print(f"Sentence: '{sentence}' has a POSITIVE sentiment. prob= {prob}")
    else:
        print(f"Sentence: '{sentence}' has a NEGATIVE sentiment.prob= {prob}")

