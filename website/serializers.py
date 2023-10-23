from marshmallow import Schema, fields




class TempReportSerializer(Schema):
    COMPANY_CODE = fields.String()
    I_OPZONE_CODE = fields.String()
    I_STATUS = fields.String()
    REGION_CODE = fields.String()
    SCHEME_CODE = fields.String()
    SEQ = fields.Integer()
    YEAR_YR = fields.Integer()
    H_AIP_DESC = fields.String()
    H_ASS_REP_REF_NO = fields.String()