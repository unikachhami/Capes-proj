import mlflow
from mlflow.tracking import MlflowClient

import mlflow
import dagshub
from mlflow.tracking import MlflowClient

mlflow.set_tracking_uri("https://dagshub.com/unikbahadur1852/Capes-proj.mlflow")

dagshub.init(repo_owner="unikbahadur1852", repo_name="Capes-proj", mlflow=True)

client = MlflowClient()

run_id = "3c66a6190a0f488584f2676445349dad"

client = MlflowClient()
artifacts = client.list_artifacts(run_id)

for a in artifacts:
    print(a.path)