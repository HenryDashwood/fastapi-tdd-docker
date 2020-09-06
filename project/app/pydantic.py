from pydantic import BaseModel


class SummaryPayloadShema(BaseModel):
    url: str
