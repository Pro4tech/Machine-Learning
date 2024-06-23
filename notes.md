# Codes:
sudo apt-get install python3
pip3 install ipython
sudo apt install python3-pip
pip3 install ipython
python -m pip install ipykernel
python3 -m pip3 install ipykernel
pip3 install matplotlib
pip3 install opencv-python

1.install py3:sudo apt-get install python3
2.#-Used for line comment
3."""----""":-Used for multi-line comment
4.While using use code-python3 'Filename'
5.In .py file array implementation is done using Lists
6.-ve index starts from a[n]->>a[0]
7.Array Range [a:b] a is included while b is not included-if a=0 the 1st element
  is not seen and if b=n then nth char is not seen
8.Parameters In print():sep=n-Is used as separator with char n && end=n-the End
  Char with char n
9.pip-It is a own repo of python related program or applications and pip3 for python3 usage
10.Packages Installed:tensorflow,cv2&matplotlib
11.fun.__doc__: allows to display the comment line
12.'+Char':Results in the concatenated string output
13.Function assignment:Normal(non-Default) Argument-->>Default Argument
14.*Argument:is used when the no of argument to be taken are not known
15.a)Tuple:They are Similar to Lists but cannot change its inner values dynamically
  .b)They can contain heterogeneous data ie mix of all possible data-types
  .c) And each element must be written with ',' between them
16.Dictionaries:It stores in key-value pair (key:value)
17.To counter Exceptions Python used Try-Except Blocks
18.__new__ :is the actual function for a Constructor

# Machine Learning:"Neural Networks in M.L"-By Vibhav
1.Tensorflow is majorly  used due to high compatibility of systems
2.Depends mainly on ANN(Neural Networks) Methods.single Neural network is called preceptron
3.In Neural Networks in graphical form :Y=mx+c is written as Y=W.X+B,Where W is
  the weight associated with the data,X:The input data and B:the bias that serves
  starting condition when
  W.X=0
4.Loss:They are mistake predicted values distance from the correct/actual values given by:
  Loss=predicted value-Actual value
5.Large loss is far more unwanted then large accuracy in output.Accuracy is of less
  imp w.r.t the rate of Loss
6.The optimum weight is calculated by using testing by arbitrary weight.The resolution
  of the change in weights is referred to as "Learning Rate" of the algo.
7.Optimizer:They are the algo(Mathematical formulae) used to
  determine the Learning Rate of the ML problem.

# Machine Learning:Programming for M.L"
1.The syntax/Language used in ML now is Keras(Tensorflow sub-set)
2.Higher no of neurons or the layer results in higher time required
3.keras.io/datasets:Data-sets for ML.If need to refer them for Understanding
4.Input:input_shape(batch-size,image-size,channel)
  a.batch-size:The number of inputs given to the program at one go.
  b.image-size:the resolution of the image(In this testing)
  c.channel:Its is required for coloured images otherwise not required
5.Hidden Layers:The layer containing the neurons
6.Dense Layer:The Hidden Layers wherein all neurons are inter-connected
              unidirectionally
7.keras.datasets:It returns two tuples[(x_train,y_train),(x_test,y_test)].....
  the earlier being the train input tuple and later being the checking tuple
8.The input Data is Being Normalized to Lower the comparison numbers
  a)Sequential:Its Shows the type of networkthat is being created(Neural Network)
9.Dense(No of Neurons,Activation Function).
  a)Higher no of layers can at time provide for higher acc and lower losses
10.a)relu:retifier linear units .Used to compute for linear Neural Network
          inputs and output to be +ve and need to be fast
   b)softmax:For probability related solution In Neural Network applications
11.Over-training of the Model will result it in remembering the exact values which is make is
   non-efficient in new Data
12.To give the shape of x_train two methods are possible:
  a)print(x_train.shape[1:])
  b)printf(x_train[n].shape)

# Image Recognization System Using ML
1.For higher resolution images,we deploy convolution logic which converts the Data into
   smaller patches of data which may be easier and faster for its Data Processing.
   Which works on a logic of creating a relation with the larger Data(Inputed Data) and the Training Data
2.Max_Pooling:Its allows in lowering the date size by finding the most prominant features in the convoluted
   data for training of the system.
3.For application on low space you can use tensorflow lite
4.a)Recurrent Neural Network:Used in Prediction system requirement.
  ->Intermediate inputs may change the Intermediate Output
  b)Feed-Forward NN:Used in image Recognization or forward driven Recognization systems requirement.
  ->Intermediate inputs may not change the the Intermediate Output
5.In RNNs They use Gated Memory Cells which stores in the Intermediate resuts for the
  ->Intermediate outputs/calculation of the weights or the Learning Rate.
  ->Its is mainly used when the order of Prediction is pretty important.
  ->Drawback:
      ->It result in a large number of layers being created
      ->Faster Saturation of the Prediction.Due to high numbers of Layer and might result in Prediction
        errors as weight associated might change exponentially
  ->The Later DB as resulted in creation of LSTM(Memory Cells).Which Hepls in retaining previous features
    weights associated with them
6.tensorboard allows for the graphical representation of the epochs
  ->to access the tensorboard output use the following code:
    ->tensorboard --logdir=/home/pritesh/Desktop/ML/python/Tensorflow/logs/digitrec
      ->for log file is in:/home/pritesh/Desktop/ML/python/Tensorflow/logs/digitrec
6.return_sequences in rnn gives output in Sequences or not if
  ->return_sequences=True gives output as Sequences while return_sequences=False,
    ->gives output as a single value
