from marshmallow import Schema, fields


class GeneralSchema(Schema):
    AppName = fields.Str() 
    ProductOwner = fields.Str()
    NamePrefix = fields.Str()
    PrimaryOperatingRegion = fields.Str()
    EnabledRegions = fields.List(fields.Str())
    MemberAccounts = fields.List(fields.Str())
