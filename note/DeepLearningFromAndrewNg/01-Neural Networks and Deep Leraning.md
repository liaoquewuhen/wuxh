[TOC]

### 1.Introduction

- 课程安排：

![image-20200606103411971](image/image-20200606103411971.png)

- ReLU(Rectified Linear Unite)：线性整流函数

<img src="image/image-20200606103802246.png" alt="image-20200606103802246" style="zoom:200%;" />

- 目前应用：

![image-20200606104536764](image/image-20200606104536764.png)

![image-20200606110306895](image/image-20200606110306895.png)

- 各类算法中数据与预测准确率的关系：

![image-20200606110946529](image/image-20200606110946529.png)



### 2.Neural Network Basics

- Binary Classification:

  - $m/m_{train}$表示训练集的样本数目
  - 将每个样本的元素reshape成列向量并将训练集中m个列向量放在一起组成一个矩阵X，在python中$X.shape=(n_x,m)$，$n_x$表示每个样本的像素总数，即$h \times w \times channels $
  - 将样本的标签排成行向量，记作Y，Y.shape=(1,m)

- Logistic Regression:

  - sigmoid function:

    ![image-20200606144241142](image/image-20200606144241142.png)

  - 将偏差放入X矩阵的表示方法：

    ![image-20200606144449598](image/image-20200606144449598.png)

- Logistic Regression cost function:

  - loss function:

    ![image-20200606145433139](image/image-20200606145433139.png)

  - cost function:

    ![image-20200606145513436](image/image-20200606145513436.png)

