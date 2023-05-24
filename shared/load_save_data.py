def save_data(data, filename):
    try:
        file = open(filename, "w")
        file.write(data)
        file.close()
    except Exception as error:
        return { "error": error }

def load_data(filename):
    data = None

    try:
        file = open(filename)
        data = file.read()
    except Exception as error:
        return { "error": error }
    
    return data
