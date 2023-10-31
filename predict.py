# Prediction interface for Cog ⚙️
# https://github.com/replicate/cog/blob/main/docs/python.md

from cog import BasePredictor, Input, Path


class Predictor(BasePredictor):
    def setup(self) -> None:
        return

    def predict(
        self,
        fear_factor: int = Input(
            description="Level of spookiness", ge=2, le=100, default=2
        ),
    ) -> str:
        return "b"+("o"*fear_factor)+"!"
        
