from pydantic import BaseModel

from pydantic import BaseModel


class input_data(BaseModel):
    radius_worst:float
    perimeter_worst:float
    area_worst:float
    perimeter_mean:float
    radius_mean:float
    area_mean:float
    concavity_worst:float
    concavity_mean:float
    concave_points_mean:float
    concave_points_worst:float

    def to_dict(self):
        return {
            "radius_worst":self.radius_worst,
            "perimeter_worst":self.perimeter_worst,
            "area_worst":self.area_worst,
            "perimeter_mean":self.perimeter_mean,
            "radius_mean":self.radius_mean,
            "area_mean":self.area_mean,
            "concavity_worst":self.concavity_worst,
            "concavity_mean":self.concavity_mean,
            "concave_points_mean":self.concave_points_mean,
            "concave_points_worst":self.concave_points_worst
        }