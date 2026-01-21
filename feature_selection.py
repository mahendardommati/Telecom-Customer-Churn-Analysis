from sklearn.feature_selection import SelectKBest, chi2

class FeatureSelector:

    def select_features(self, X, y, k=10):
        try:
            selector = SelectKBest(score_func=chi2, k=k)
            X_new = selector.fit_transform(X, y)
            return X_new
        except Exception as e:
            raise Exception(f"Feature selection error: {e}")
