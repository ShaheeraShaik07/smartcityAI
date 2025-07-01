from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai import Credentials

API_KEY = "rSB9rGwsEuCQxdQkl1JwzA0nKBFT_rHAuu0tomv_ZtQD"
PROJECT_ID = "9b4bbea6-1b7a-406d-b622-6989085907d2"
MODEL_ID = "ibm-granite/granite-3.3-2b-instruct"

def query_granite(prompt: str) -> str:
    credentials = Credentials(api_key=API_KEY)
    model = Model(model_id=MODEL_ID, credentials=credentials, params={"decoding_method": "sample", "max_new_tokens": 100})
    result = model.generate(prompt=prompt, project_id=PROJECT_ID)
    return result.get("generated_text", "No response")