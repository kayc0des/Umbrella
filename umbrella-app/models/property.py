from basemodel import BaseModel

class Property(BaseModel):

    property_name = ""
    property_category = ""
    property_description = ""
    property_price = ""
    property_fraction = ""
    property_slots = ""
    property_status = ""

    def fractional_price(self):
        price = float(self.property_price)
        fractions = float(self.property_fraction)
        fractional_price = price / fractions
        return fractional_price

property1 = Property()
property1.save()