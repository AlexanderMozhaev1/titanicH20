from h2o.automl import H2OAutoML


def train(y, df):
    aml = H2OAutoML(max_models=100, max_runtime_secs=600, seed=22)
    aml.train(y=y, training_frame=df)
    return aml
