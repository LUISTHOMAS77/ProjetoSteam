class import_data:

## teste inclusão
    def __init__(self, path):
        self.path = path
        self.data = pd.read_csv(self.path)
        self.data = self.data.dropna()