import pickle


def loadModel(fileName):
    try:
        with open(fileName, 'rb') as file:
            model = pickle.load(file)
        print("Model loaded successfully.")
        return model
    except FileNotFoundError:
        print("Model file not found.")
    except Exception as e:
        print("Error while loading the model.", str(e))


model = loadModel(r"E:\programming\python\pythonProject6\model.pkl")
input_data = [[6, 147, 72, 35, 0, 33.6, 0.627, 50]]  # Example input data
predictions = model.predict(input_data)
print(predictions)
