from h2o.automl import H2OAutoML


def train(y, df, params):
    aml = H2OAutoML(max_models=params['max_models'],
                    max_runtime_secs=params['max_runtime_secs'],
                    seed=params['seed'])
    aml.train(y=y, training_frame=df)
    return aml