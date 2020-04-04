#Build Feature_Selector class
from sklearn.base import BaseEstimator, TransformerMixin

class FeatureSelector(BaseEstimator, TransformerMixin):
    '''
    Select certain features from a Dataframe, return numpy array
    '''
    def __init__(self, columns):
        '''
        columns: list of columns
        '''
        self.columns = columns
        
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y = None):
        return X.loc[:, self.columns].values.reshape(-1, len(self.columns))