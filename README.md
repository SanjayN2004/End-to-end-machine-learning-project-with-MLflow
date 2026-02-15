# End-to-end-machine-learning-project-with-MLflow


import dagshub
dagshub.init(repo_owner='sanjayncse2021', repo_name='End-to-end-machine-learning-project-with-MLflow', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)


  https://dagshub.com/sanjayncse2021/End-to-end-machine-learning-project-with-MLflow.mlflow