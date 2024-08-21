class Supplier:
    def __init__(self):
        # The key is the API key for the-odds-api at https://the-odds-api.com/#get-access
        self.key = ""
        
        # The directory is the location of the projections.json file
        self.directory = ""
        
    def get_key(self):
        return self.key
    
    def get_directory(self):
        return self.directory