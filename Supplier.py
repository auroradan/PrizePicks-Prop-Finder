class Supplier:
    def __init__(self):
        # The key is the API key for the-odds-api at https://the-odds-api.com/#get-access
        self.key = "170979f3fa7d22479123bc8d7b9e2c3a"
        
        # The directory is the location of the projections.json file
        self.directory = "C:\\Users\\dantr\\Downloads\\projections.json"
        
    def get_key(self):
        return self.key
    
    def get_directory(self):
        return self.directory