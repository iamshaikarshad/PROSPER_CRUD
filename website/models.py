from . import db
from flask_login import UserMixin
from sqlalchemy import Column, Date, Integer, MetaData, String, Table, DateTime
from flask_marshmallow import Marshmallow

metadata = MetaData()

class cac():
  pass

class TEST(db.Model):
  __tablename__ = 'my_tablename'
  __table_args__ = {"schema": "PROSPER"} 
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  description = db.Column(db.String(255)) 



class Incidents_stage1(db.Model):
  __tablename__ = 'INCIDENTS_STAGE1'
  __table_args__ = {"schema": "PROSPER"} 
  COMPANY_CODE = db.Column(db.String(2), nullable=False)#nn
  I_OPZONE_CODE = db.Column(db.String(4), nullable=False)
  I_STATUS = db.Column(db.String(1), nullable=False)
  REGION_CODE = db.Column(db.String(2), nullable=False)
  SCHEME_CODE = db.Column(db.String(2), nullable=False)
  SEQ = db.Column(db.Integer, nullable=False)
  YEAR_YR = db.Column(db.Integer, nullable=False)
  H_AIP_DESC = db.Column(db.String(40))
  H_ASS_REP_REF_NO = db.Column(db.String(32))
  H_AUTO_ISOL_POINT = db.Column(db.String(35))
  H_AUTO_ISOL_POINT_UDB = db.Column(db.String(18))
  H_AUTO_SWITCH1 = db.Column(db.String(32))
  H_AUTO_SWITCH2 = db.Column(db.String(32))
  H_NEAR_ISOL_POINT = db.Column(db.String(35))
  H_NEAR_ISOL_POINT_UDB = db.Column(db.String(18))
  H_NIP_DESC = db.Column(db.String(40))
  H_TOT_LOAD_LOST_MVA = db.Column(db.Integer)
  HL_JOB_REF_NO = db.Column(db.String(32),primary_key=True)
  I_ASSOC_INCI_REGION = db.Column(db.String(2))
  I_ASSOC_INCI_SEQ = db.Column(db.Integer)
  I_ASSOC_NUM = db.Column(db.Integer)
  I_BOX_1 = db.Column(db.String(32))
  I_BOX_2 = db.Column(db.String(32))
  I_BOX_3 = db.Column(db.String(32))
  I_BOX_4 = db.Column(db.String(32))
  I_BOX_5 = db.Column(db.String(32))
  I_BOX_6 = db.Column(db.String(32))
  I_CAUSE_CODE_1 = db.Column(db.String(2))
  I_CLOSED_FLAG = db.Column(db.String(1))
  I_CONS_HRS = db.Column(db.Integer)
  I_CONS_NUM = db.Column(db.Integer)
  I_DURATION_HRS = db.Column(db.Integer)
  I_EARLIEST_INTERRUPT_DATE = db.Column(db.DateTime)
  I_EARLIEST_RESTORE_DATE = db.Column(db.DateTime)
  I_EC_BOX1 = db.Column(db.String(2))
  I_FAILED_VALIDATION = db.Column(db.String(1))
  I_INC_DATE_TIME = db.Column(db.DateTime)
  I_LAST_UPDATED = db.Column(db.DateTime)
  I_LATEST_INTERRUPT_DATE = db.Column(db.DateTime)
  I_LATEST_RESTORE_DATE = db.Column(db.DateTime)
  I_MAIN_CIRCUIT = db.Column(db.String(35))
  I_MAIN_CIRCUIT_CODE_UDB = db.Column(db.String(18))
  I_MAX_RS_NUM = db.Column(db.Integer)
  I_MC_DESC = db.Column(db.String(40))
  I_MIN_RS_NUM = db.Column(db.Integer)
  I_REPORT_DATE_TIME = db.Column(db.DateTime)
  I_REST_NUM = db.Column(db.Integer)
  I_RS_MAX_DURATION_CONS_NUM = db.Column(db.Integer)
  I_RS_MAX_DURATION_HRS = db.Column(db.Integer)
  I_RS_NUM_OF_MAX_DURATION = db.Column(db.Integer)
  I_TCMS = db.Column(db.String(32))
  I_VOLTAGE_1 = db.Column(db.String(3))
  K_CIRCUIT_ID = db.Column(db.String(4))
  K_ENG_NAME2 = db.Column(db.String(20))
  K_ENG_NAME3 = db.Column(db.String(20))
  K_ENG_NAME4 = db.Column(db.String(20))
  K_ENG_NAME5 = db.Column(db.String(20))
  K_ENG_NAME6 = db.Column(db.String(20))
  K_NO_RECALC = db.Column(db.String(1))
  K_PERFORM_1 = db.Column(db.String(2))
  K_PERFORM_2 = db.Column(db.String(2))
  K_PERFORM_COMMENT = db.Column(db.String(160))
  K_RELAY_IND_TITLE = db.Column(db.String(72))
  K_SWITCH_ID = db.Column(db.String(6))
  K_TRANS_ID = db.Column(db.String(5))
  K_TRANS_RATE_OPTION = db.Column(db.String(6))
  KH_CAUSE_CODE_2 = db.Column(db.String(2))
  KH_COMPONENT_CODE = db.Column(db.String(3))
  KH_DAM_COMP_1 = db.Column(db.String(3))
  KH_DAM_COMP_2 = db.Column(db.String(3))
  KH_DAM_COMP_3 = db.Column(db.String(3))
  KH_DAMAGE = db.Column(db.String(130))
  KH_DANGEROUS = db.Column(db.String(1))
  KH_DESC = db.Column(db.String(255))
  KH_DISTANCE_KM = db.Column(db.Integer)
  KH_EC_BOX2 = db.Column(db.String(2))
  KH_EC_BOX3 = db.Column(db.String(2))
  KH_EC_BOX4 = db.Column(db.String(3))
  KH_ENG_DESIG = db.Column(db.String(25))
  KH_ENG_NAME = db.Column(db.String(25))
  KH_MAKER_TYPE = db.Column(db.String(8))
  KH_MEI = db.Column(db.String(6))
  KH_MEI1 = db.Column(db.String(1))
  KH_OVERHEAD_CONDUCTOR = db.Column(db.String(1))
  KH_OVERHEAD_LINE_PROX = db.Column(db.String(1))
  KH_OVERHEAD_SPACING = db.Column(db.String(1))
  KH_OVERHEAD_SPAN = db.Column(db.String(3))
  KH_SITE_CODE = db.Column(db.String(7))
  KH_SITE_DESC = db.Column(db.String(255))
  KH_STATE_OF_PROGRESS_CODE = db.Column(db.String(2))
  KH_STATUS1 = db.Column(db.String(1))
  KH_STATUS2 = db.Column(db.String(1))
  KH_STATUS3 = db.Column(db.String(1))
  KH_TOT_MAX_DEMAND = db.Column(db.Integer)
  KH_VOLTAGE_2 = db.Column(db.String(3))
  KHL_DAMAGE_CAUSE = db.Column(db.String(255))
  KHL_MAKER_NAME = db.Column(db.String(20))
  KHL_MANUFACTUR_CODE = db.Column(db.String(3))
  KHL_YEAR_MADE = db.Column(db.String(4))
  L_CLASS_CODE = db.Column(db.String(1))
  L_COMPONENT_CODE = db.Column(db.String(1))
  L_FEEDER = db.Column(db.String(2))
  L_FLAG1 = db.Column(db.String(1))
  L_FLAG2 = db.Column(db.String(1))
  L_FUSE_INV = db.Column(db.String(16))
  L_INCOMER = db.Column(db.String(2))
  L_INJURY = db.Column(db.String(1))
  L_MEI = db.Column(db.String(2))
  L_MEI1 = db.Column(db.String(1))
  L_PHASE = db.Column(db.String(3))
  L_RECHARGEABLE = db.Column(db.String(1))
  L_SECONDARY_ALIAS_UDB = db.Column(db.String(18))
  L_SUBSTAT_ID = db.Column(db.String(8))
  L_SUBSTAT_NAME = db.Column(db.String(128))
  METH_CLEAR_FAULT = db.Column(db.String(2))
  METH_CLEAR_FAULT2 = db.Column(db.String(2))
  NP_BOX1 = db.Column(db.String(1))
  NP_BOX2 = db.Column(db.String(2))
  NP_BOX3 = db.Column(db.String(3))
  NP_BOX4 = db.Column(db.String(4))
  PANP_ADVICE_METHOD = db.Column(db.String(1))
  PANP_SCHEME = db.Column(db.String(2))
  REPORTING_SCHEME = db.Column(db.String(10))
  TCALL_OPZONE = db.Column(db.String(4))
  TEMP_REGION = db.Column(db.String(2))
  TEMP_SEQ = db.Column(db.Integer)
  TEMP_YEAR = db.Column(db.Integer)
  SOURCE_SCHEME = db.Column(db.String(3))
  JOB_STATUS = db.Column(db.String(1))
  SPLIT_INCIDENT = db.Column(db.String(1))
  SI_TYPE = db.Column(db.String(1))
  SI_TRIPS_TO_LOCK = db.Column(db.Integer)
  SI_TRIPS = db.Column(db.Integer)
  CUSTOMERS_INTERRUPTED = db.Column(db.Integer)
  L_SUBSTAT_CUSTS = db.Column(db.String(6))
  SI_CAUSE_CODE = db.Column(db.String(10))
  REINTERRUPTION = db.Column(db.String(1))




# class uncident_stage1():
#     t_INCIDENTS_STAGE1 = Table(
#     'INCIDENTS_STAGE1', metadata,
#     Column('COMPANY_CODE', String(2, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
#     Column('I_OPZONE_CODE', String(4, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
#     Column('I_STATUS', String(1, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
#     Column('REGION_CODE', String(2, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
#     Column('SCHEME_CODE', String(2, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
#     Column('SEQ', Integer, nullable=False),
#     Column('YEAR_YR', Integer, nullable=False),
#     Column('H_AIP_DESC', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('H_ASS_REP_REF_NO', String(32, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('H_AUTO_ISOL_POINT', String(35, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('H_AUTO_ISOL_POINT_UDB', String(18, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('H_AUTO_SWITCH1', String(32, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('H_AUTO_SWITCH2', String(32, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('H_NEAR_ISOL_POINT', String(35, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('H_NEAR_ISOL_POINT_UDB', String(18, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('H_NIP_DESC', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('H_TOT_LOAD_LOST_MVA', Integer),
#     Column('HL_JOB_REF_NO', String(32, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('I_ASSOC_INCI_REGION', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('I_ASSOC_INCI_SEQ', Integer),
#     Column('I_ASSOC_NUM', Integer),
#     Column('I_BOX_1', String(32, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('I_BOX_2', String(32, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('I_BOX_3', String(32, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('I_BOX_4', String(32, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('I_BOX_5', String(32, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('I_BOX_6', String(32, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('I_CAUSE_CODE_1', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('I_CLOSED_FLAG', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('I_CONS_HRS', Integer),
#     Column('I_CONS_NUM', Integer),
#     Column('I_DURATION_HRS', Integer),
#     Column('I_EARLIEST_INTERRUPT_DATE', Date),
#     Column('I_EARLIEST_RESTORE_DATE', Date),
#     Column('I_EC_BOX1', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('I_FAILED_VALIDATION', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('I_INC_DATE_TIME', Date),
#     Column('I_LAST_UPDATED', Date),
#     Column('I_LATEST_INTERRUPT_DATE', Date),
#     Column('I_LATEST_RESTORE_DATE', Date),
#     Column('I_MAIN_CIRCUIT', String(35, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('I_MAIN_CIRCUIT_CODE_UDB', String(18, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('I_MAX_RS_NUM', Integer),
#     Column('I_MC_DESC', String(40, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('I_MIN_RS_NUM', Integer),
#     Column('I_REPORT_DATE_TIME', Date),
#     Column('I_REST_NUM', Integer),
#     Column('I_RS_MAX_DURATION_CONS_NUM', Integer),
#     Column('I_RS_MAX_DURATION_HRS', Integer),
#     Column('I_RS_NUM_OF_MAX_DURATION', Integer),
#     Column('I_TCMS', String(32, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('I_VOLTAGE_1', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('K_CIRCUIT_ID', String(4, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('K_ENG_NAME2', String(20, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('K_ENG_NAME3', String(20, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('K_ENG_NAME4', String(20, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('K_ENG_NAME5', String(20, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('K_ENG_NAME6', String(20, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('K_NO_RECALC', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('K_PERFORM_1', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('K_PERFORM_2', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('K_PERFORM_COMMENT', String(160, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('K_RELAY_IND_TITLE', String(72, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('K_SWITCH_ID', String(6, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('K_TRANS_ID', String(5, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('K_TRANS_RATE_OPTION', String(6, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KH_CAUSE_CODE_2', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KH_COMPONENT_CODE', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KH_DAM_COMP_1', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KH_DAM_COMP_2', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KH_DAM_COMP_3', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KH_DAMAGE', String(130, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KH_DANGEROUS', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KH_DESC', String(255, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KH_DISTANCE_KM', Integer),
#     Column('KH_EC_BOX2', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KH_EC_BOX3', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KH_EC_BOX4', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KH_ENG_DESIG', String(25, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KH_ENG_NAME', String(25, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KH_MAKER_TYPE', String(8, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KH_MEI', String(6, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KH_MEI1', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KH_OVERHEAD_CONDUCTOR', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KH_OVERHEAD_LINE_PROX', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KH_OVERHEAD_SPACING', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KH_OVERHEAD_SPAN', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KH_SITE_CODE', String(7, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KH_SITE_DESC', String(255, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KH_STATE_OF_PROGRESS_CODE', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KH_STATUS1', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KH_STATUS2', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KH_STATUS3', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KH_TOT_MAX_DEMAND', Integer),
#     Column('KH_VOLTAGE_2', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KHL_DAMAGE_CAUSE', String(255, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KHL_MAKER_NAME', String(20, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KHL_MANUFACTUR_CODE', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('KHL_YEAR_MADE', String(4, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('L_CLASS_CODE', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('L_COMPONENT_CODE', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('L_FEEDER', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('L_FLAG1', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('L_FLAG2', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('L_FUSE_INV', String(16, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('L_INCOMER', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('L_INJURY', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('L_MEI', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('L_MEI1', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('L_PHASE', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('L_RECHARGEABLE', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('L_SECONDARY_ALIAS_UDB', String(18, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('L_SUBSTAT_ID', String(8, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('L_SUBSTAT_NAME', String(128, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('METH_CLEAR_FAULT', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('METH_CLEAR_FAULT2', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('NP_BOX1', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('NP_BOX2', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('NP_BOX3', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('NP_BOX4', String(4, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('PANP_ADVICE_METHOD', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('PANP_SCHEME', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('REPORTING_SCHEME', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('TCALL_OPZONE', String(4, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('TEMP_REGION', String(2, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('TEMP_SEQ', Integer),
#     Column('TEMP_YEAR', Integer),
#     Column('SOURCE_SCHEME', String(3, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('JOB_STATUS', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('SPLIT_INCIDENT', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('SI_TYPE', String(1, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('SI_TRIPS_TO_LOCK', Integer),
#     Column('SI_TRIPS', Integer),
#     Column('CUSTOMERS_INTERRUPTED', Integer),
#     Column('L_SUBSTAT_CUSTS', String(6,'SQL_Latin1_General_CP1_CI_AS')),
#     Column('SI_CAUSE_CODE', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
#     Column('REINTERRUPTION', String(1, 'SQL_Latin1_General_CP1_CI_AS'))
# )