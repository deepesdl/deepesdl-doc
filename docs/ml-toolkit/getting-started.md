# Getting Started with ML Toolkit

All Jupyter Notebooks follow the same architecture involving the five major sections:


	1. Import necessary libraries and helperfunctions
	2. Load data (Earth System Data Cube, s3 object store)
		* Air Temperature
		* Land Surface Temperature
	3. Train/test split (0.8/0.2)
		* efficient block sampling
	4. Model set-up (linear regression with 1 node/ shallow neural network)
	5. Iteration over blocks and subsequent random sampling
		* Preprocessing (filtering NaNs, standardization, normalization)
		* Get train/test data
		* Generate training batches using existing data loading and transformation mechanisms from Keras and PyTorch (DataGenerator, DataLoader)
		* Train model, return error and loss
		* Evaluate Model
	


<!--It is mandatory to enable machine learning that respects the basic principles of geo-data way beyond naive applications of 
machine learning in the Earth system context. To avoid auto-correlation during the training phase of the model, data sampling is 
guided by a block sampling strategy. Data blocks are rectangularly shaped varying in size and amount of data points. -->
