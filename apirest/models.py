# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AppPermArtAditionals(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    type_data = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_ART_aditionals'


class AppPermArtAssociatedEquipments(models.Model):
    id = models.BigAutoField(primary_key=True)
    detail = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    inspection_monthly = models.BooleanField()
    associated_verification = models.BooleanField()
    head_art = models.ForeignKey('AppPermArtHeads', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_ART_associated_equipments'


class AppPermArtControls(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS')
    step = models.ForeignKey('AppPermArtSteps', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_ART_controls'


class AppPermArtCrossRegisters(models.Model):
    id = models.BigAutoField(primary_key=True)
    area = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    work_1 = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    work_2 = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    work_3 = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    url_image = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    url_audio = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    id_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_user', blank=True, null=True)
    head_art = models.ForeignKey('AppPermArtHeads', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_ART_cross_registers'


class AppPermArtEmployees(models.Model):
    id = models.BigAutoField(primary_key=True)
    position = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    type_data = models.IntegerField(blank=True, null=True)
    url_image = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    url_audio = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    id_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_user', blank=True, null=True)
    head_art = models.ForeignKey('AppPermArtHeads', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_ART_employees'


class AppPermArtEppRiskStep(models.Model):
    id = models.BigAutoField(primary_key=True)
    step = models.ForeignKey('AppPermArtSteps', models.DO_NOTHING)
    epp_risk = models.ForeignKey('AppPermEppRisks', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_ART_epp_risk_step'


class AppPermArtHeadAdditional(models.Model):
    id = models.BigAutoField(primary_key=True)
    additional = models.ForeignKey(AppPermArtAditionals, models.DO_NOTHING)
    head_art = models.ForeignKey('AppPermArtHeads', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_ART_head_additional'


class AppPermArtHeadRiskRule(models.Model):
    id = models.BigAutoField(primary_key=True)
    risk_rule = models.ForeignKey('AppPermArtRiskRules', models.DO_NOTHING)
    head_art = models.ForeignKey('AppPermArtHeads', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_ART_head_risk_rule'


class AppPermArtHeads(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    date = models.DateField()
    activity_name = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    interactive_work = models.BooleanField()
    area = models.ForeignKey('AppPermAreas', models.DO_NOTHING)
    company = models.ForeignKey('AppPermCompanies', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_ART_heads'


class AppPermArtRiskRules(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    icon = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    type_data = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_ART_risk_rules'


class AppPermArtSteps(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_ART_steps'


class AppPermCepActivities(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_CEP_activities'


class AppPermCepAuthorizationStaff(models.Model):
    id = models.BigAutoField(primary_key=True)
    location_test = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    name = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    number_lock = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    url_image = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    url_audio = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    head_detail = models.ForeignKey('AppPermCepHeadDetail', models.DO_NOTHING)
    speciality_type = models.ForeignKey('AppPermCepSpecialitiesTypes', models.DO_NOTHING)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_CEP_authorization_staff'


class AppPermCepBlockEquipments(models.Model):
    id = models.BigAutoField(primary_key=True)
    tag = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    number_lock = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    equipment_state = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    test = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    area = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    head_detail = models.ForeignKey('AppPermCepHeadDetail', models.DO_NOTHING)
    energy_type = models.ForeignKey('AppPermCepEnergyTypes', models.DO_NOTHING)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_CEP_block_equipments'


class AppPermCepEnergyTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_CEP_energy_types'


class AppPermCepHeadDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    name_activity = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    area = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    gf_eecc = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    procedure_activity = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    verify_erc = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    time_block_hours = models.IntegerField(blank=True, null=True)
    time_block_minutes = models.IntegerField(blank=True, null=True)
    n_ot = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    location_block = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    observations = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    type_data = models.IntegerField(blank=True, null=True)
    head = models.ForeignKey('AppPermCepHeads', models.DO_NOTHING)
    activity = models.ForeignKey(AppPermCepActivities, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_CEP_head_detail'


class AppPermCepHeads(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_CEP_heads'


class AppPermCepSpecialitiesTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_CEP_specialities_types'


class AppPermCepStaffs(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    position = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    observations = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    type_data = models.IntegerField(blank=True, null=True)
    url_image = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    url_audio = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    head_detail = models.ForeignKey(AppPermCepHeadDetail, models.DO_NOTHING)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_CEP_staffs'


class AppPermEcAssesstments(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    porcentaje = models.FloatField(blank=True, null=True)
    ppm = models.FloatField(blank=True, null=True)
    head = models.ForeignKey('AppPermEcHeads', models.DO_NOTHING)
    gas = models.ForeignKey('AppPermEcGases', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_EC_assesstments'


class AppPermEcAutorizationEmployees(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    position = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    type_data = models.IntegerField(blank=True, null=True)
    url_image = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    url_audio = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    head = models.ForeignKey('AppPermEcHeads', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_EC_autorization_employees'


class AppPermEcCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_EC_categories'


class AppPermEcGases(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    limit = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    type_data = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_EC_gases'


class AppPermEcHeadOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    boolean_check = models.BooleanField(blank=True, null=True)
    additional = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    head = models.ForeignKey('AppPermEcHeads', models.DO_NOTHING)
    option = models.ForeignKey('AppPermEcOptions', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_EC_head_options'


class AppPermEcHeads(models.Model):
    id = models.BigAutoField(primary_key=True)
    company = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    ast = models.BooleanField(blank=True, null=True)
    procedure = models.BooleanField(blank=True, null=True)
    erc = models.BooleanField(blank=True, null=True)
    description = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_EC_heads'


class AppPermEcOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    type_data = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(AppPermEcCategories, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_EC_options'


class AppPermEcPermissionValidate(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    position = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    description = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    url_image = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    url_audio = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    head = models.ForeignKey(AppPermEcHeads, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_EC_permission_validate'


class AppPermIzaesCapacityLoading(models.Model):
    id = models.BigAutoField(primary_key=True)
    weight_net = models.FloatField(blank=True, null=True)
    weight_accessory = models.FloatField(blank=True, null=True)
    weight_equipment = models.FloatField(blank=True, null=True)
    weight_other = models.FloatField(blank=True, null=True)
    weight_total = models.FloatField(blank=True, null=True)
    weight_estimated = models.FloatField(blank=True, null=True)
    image = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    head = models.ForeignKey('AppPermIzaesHeads', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_IZAES_capacity_loading'


class AppPermIzaesConditionHead(models.Model):
    id = models.BigAutoField(primary_key=True)
    option_bool = models.BooleanField(blank=True, null=True)
    head = models.ForeignKey('AppPermIzaesHeads', models.DO_NOTHING)
    condition = models.ForeignKey('AppPermIzaesConditions', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_IZAES_condition_head'


class AppPermIzaesConditions(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_IZAES_conditions'


class AppPermIzaesFinalLoading(models.Model):
    id = models.BigAutoField(primary_key=True)
    estimated_weight = models.FloatField(blank=True, null=True)
    capacity_table_loading = models.FloatField(blank=True, null=True)
    capacity_charge_percent = models.FloatField(blank=True, null=True)
    number_75_boolean = models.BooleanField(db_column='75_boolean', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    head = models.ForeignKey('AppPermIzaesHeads', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_IZAES_final_loading'


class AppPermIzaesHeads(models.Model):
    id = models.BigAutoField(primary_key=True)
    company_activity = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    date_maneuver = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    equipment = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    equipment_brand = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    ast = models.BooleanField(blank=True, null=True)
    procedure = models.BooleanField(blank=True, null=True)
    erc = models.BooleanField(blank=True, null=True)
    details = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_IZAES_heads'


class AppPermIzaesIzajeElements(models.Model):
    id = models.BigAutoField(primary_key=True)
    accessory = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    dimension = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    angle_work = models.FloatField(blank=True, null=True)
    capacity_loading = models.FloatField(blank=True, null=True)
    head = models.ForeignKey(AppPermIzaesHeads, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_IZAES_izaje_elements'


class AppPermIzaesManeuverParameter(models.Model):
    id = models.BigAutoField(primary_key=True)
    radio_operation_start = models.FloatField(blank=True, null=True)
    radio_operation_end = models.FloatField(blank=True, null=True)
    pen_length_start = models.FloatField(blank=True, null=True)
    pen_length_end = models.FloatField(blank=True, null=True)
    operating_angle_start = models.FloatField(blank=True, null=True)
    operating_angle_end = models.FloatField(blank=True, null=True)
    capacity_charge_start = models.FloatField(blank=True, null=True)
    capacity_charge_end = models.FloatField(blank=True, null=True)
    head = models.ForeignKey(AppPermIzaesHeads, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_IZAES_maneuver_parameter'


class AppPermIzaesManeuvers(models.Model):
    id = models.BigAutoField(primary_key=True)
    position_type = models.IntegerField(blank=True, null=True)
    url_image = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    url_audio = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    type_data = models.IntegerField(blank=True, null=True)
    head = models.ForeignKey(AppPermIzaesHeads, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_IZAES_maneuvers'


class AppPermIzaesWindConditions(models.Model):
    id = models.BigAutoField(primary_key=True)
    time = models.TimeField(blank=True, null=True)
    measurement = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    head = models.ForeignKey(AppPermIzaesHeads, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_IZAES_wind_conditions'


class AppPermTaAuthorizationEmployees(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS')
    position = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    type_data = models.IntegerField()
    url_image = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    url_audio = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    head_ta = models.ForeignKey('AppPermTaHeads', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_TA_authorization_employees'


class AppPermTaCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_TA_categories'


class AppPermTaControlMeasures(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS')
    category = models.ForeignKey(AppPermTaCategories, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_TA_control_measures'


class AppPermTaHeadControlMeasure(models.Model):
    id = models.BigAutoField(primary_key=True)
    boolean_check = models.IntegerField()
    control_measure = models.ForeignKey(AppPermTaControlMeasures, models.DO_NOTHING)
    head_ta = models.ForeignKey('AppPermTaHeads', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_TA_head_control_measure'


class AppPermTaHeads(models.Model):
    id = models.BigAutoField(primary_key=True)
    company = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    date = models.DateField()
    location = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    ast = models.BooleanField()
    procedure = models.BooleanField()
    erc = models.BooleanField()
    description = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_TA_heads'


class AppPermTaPermissionValidates(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    position = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    date = models.DateField()
    time = models.TimeField()
    description = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')
    url_image = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    url_audio = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    head_ta = models.ForeignKey(AppPermTaHeads, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_TA_permission_validates'


class AppPermTaRiskDangers(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    control = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    check_value = models.BooleanField(db_column='check')
    head_ta = models.ForeignKey(AppPermTaHeads, models.DO_NOTHING)
    type_data = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_TA_risk_dangers'


class AppPermAreas(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_areas'


class AppPermCompanies(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_companies'


class AppPermEppRisks(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    type_data = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_epp_risks'


class AppPermHeadPermission(models.Model):
    id = models.BigAutoField(primary_key=True)
    headtable_type = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    headtable_id = models.BigIntegerField()
    permission = models.ForeignKey('AppPermPermissions', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_head_permission'


class AppPermPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    image = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    description = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APP_PERM_permissions'


class ActionShape(models.Model):
    id = models.BigAutoField(primary_key=True)
    action = models.ForeignKey('Actions', models.DO_NOTHING)
    shape = models.ForeignKey('Shapes', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'action_shape'


class Actions(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    content = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    type_action = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actions'


class Attachments(models.Model):
    id = models.BigAutoField(primary_key=True)
    format = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    url = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    model_type = models.IntegerField(blank=True, null=True)
    attachmentable_type = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    attachmentable_id = models.BigIntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attachments'


class Backups(models.Model):
    id = models.BigAutoField(primary_key=True)
    route = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    status = models.BooleanField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'backups'


class Capsules(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    url_image = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    link = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'capsules'


class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    code = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class DetailsProgress(models.Model):
    id = models.BigAutoField(primary_key=True)
    progress = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    last_progress = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    error_points = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    game_time = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    completado = models.BooleanField(blank=True, null=True)
    progress_0 = models.ForeignKey('Progress', models.DO_NOTHING, db_column='progress_id')  # Field renamed because of name conflict.
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'details_progress'


class EquipmentTechnicalObject(models.Model):
    id = models.BigAutoField(primary_key=True)
    equipment = models.ForeignKey('Equipments', models.DO_NOTHING)
    technical_object = models.ForeignKey('TechnicalObjects', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipment_technical_object'


class EquipmentVirtualPlant(models.Model):
    id = models.BigAutoField(primary_key=True)
    equipment = models.ForeignKey('Equipments', models.DO_NOTHING)
    virtual_plant = models.ForeignKey('VirtualPlants', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipment_virtual_plant'


class Equipments(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    name_english = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    main = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    cover = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    gift = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description_1 = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description_2 = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    file = models.ForeignKey('Files', models.DO_NOTHING, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipments'


class ExamQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    exam = models.ForeignKey('Exams', models.DO_NOTHING)
    question = models.ForeignKey('Questions', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_question'


class ExamQuestionParents(models.Model):
    id = models.BigAutoField(primary_key=True)
    number_questions = models.IntegerField()
    type = models.IntegerField()
    exam = models.ForeignKey('Exams', models.DO_NOTHING)
    level = models.ForeignKey('Levels', models.DO_NOTHING, blank=True, null=True)
    file = models.ForeignKey('Files', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_question_parents'


class ExamResults(models.Model):
    id = models.BigAutoField(primary_key=True)
    correct = models.IntegerField(blank=True, null=True)
    incorrect = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    state = models.IntegerField()
    exam = models.ForeignKey('Exams', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_results'


class ExamTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_types'


class Exams(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    begind_date = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    end_date = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    state = models.IntegerField()
    exam_type = models.ForeignKey(ExamTypes, models.DO_NOTHING, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exams'


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    connection = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    queue = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    payload = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    exception = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class Files(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    description = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    tag = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    code_primary = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    code_secondary = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    icon_url = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    cover_url = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    documenttype = models.IntegerField(db_column='documentType', blank=True, null=True)  # Field name made lowercase.
    file_url = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    slug = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    level = models.ForeignKey('Levels', models.DO_NOTHING, blank=True, null=True)
    is_pdf = models.BooleanField(blank=True, null=True)
    is_video = models.BooleanField(blank=True, null=True)
    have_questions = models.BooleanField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'files'


class Historicals(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    tag = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    cover_url = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    file_url = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    revision = models.IntegerField()
    principal = models.BooleanField(blank=True, null=True)
    file = models.ForeignKey(Files, models.DO_NOTHING)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historicals'


class Icons(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    tag = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    url = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icons'


class Images(models.Model):
    id = models.BigAutoField(primary_key=True)
    format = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    url = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    level = models.ForeignKey('Levels', models.DO_NOTHING)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'images'


class Interlug(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_shape_from = models.ForeignKey('Shapes', models.DO_NOTHING, db_column='id_shape_from', related_name='id_shape_from')
    id_shape_to = models.ForeignKey('Shapes', models.DO_NOTHING, db_column='id_shape_to', related_name='id_shape_to')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interlug'


class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    queue = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    payload = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    attempts = models.SmallIntegerField()
    reserved_at = models.IntegerField(blank=True, null=True)
    available_at = models.IntegerField()
    created_at = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jobs'


class Levels(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    imgurl = models.TextField(db_column='imgUrl', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    slug = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'levels'


class MapShape(models.Model):
    id = models.BigAutoField(primary_key=True)
    shape = models.ForeignKey('Shapes', models.DO_NOTHING)
    map = models.ForeignKey('Maps', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'map_shape'


class MapTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'map_types'


class Maps(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    title = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    tag = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    image_url = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    imagesvg_url = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    type_data = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    location = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    coordinates = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    color = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    procedure = models.ForeignKey('Procedures', models.DO_NOTHING)
    type = models.ForeignKey(MapTypes, models.DO_NOTHING)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maps'


class Migrations(models.Model):
    migration = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class Options(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    answer = models.IntegerField(blank=True, null=True)
    question = models.ForeignKey('Questions', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'options'


class PasswordResets(models.Model):
    email = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    token = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class PermissionRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    role = models.ForeignKey('Roles', models.DO_NOTHING)
    permission = models.ForeignKey('Permissions', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permission_role'


class Permissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    slug = models.CharField(unique=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions'


class PlantItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    name_english = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    item_id = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    virtual_plant = models.ForeignKey('VirtualPlants', models.DO_NOTHING, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plant_item'


class PlantItemFile(models.Model):
    id = models.BigAutoField(primary_key=True)
    plant_item = models.ForeignKey(PlantItem, models.DO_NOTHING)
    file = models.ForeignKey(Files, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plant_item_file'


class Procedures(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    code = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    file = models.ForeignKey(Files, models.DO_NOTHING)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procedures'


class Progress(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    capsule = models.ForeignKey(Capsules, models.DO_NOTHING, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'progress'


class QuestionLevels(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_levels'


class QuestionResults(models.Model):
    id = models.BigAutoField(primary_key=True)
    answer = models.IntegerField()
    question = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    option = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    exam_result = models.ForeignKey(ExamResults, models.DO_NOTHING)
    question_0 = models.ForeignKey('Questions', models.DO_NOTHING, db_column='question_id')  # Field renamed because of name conflict.
    option_0 = models.ForeignKey(Options, models.DO_NOTHING, db_column='option_id', blank=True, null=True)  # Field renamed because of name conflict.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_results'


class Questions(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    file = models.ForeignKey(Files, models.DO_NOTHING)
    question_level = models.ForeignKey(QuestionLevels, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questions'


class RoleUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    role = models.ForeignKey('Roles', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role_user'


class Roles(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    slug = models.CharField(unique=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    full_access = models.BooleanField(db_column='full-access', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    system_type = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class ScoreDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    level = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    score = models.IntegerField()
    score_0 = models.ForeignKey('Scores', models.DO_NOTHING, db_column='score_id')  # Field renamed because of name conflict.
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'score_details'


class Scores(models.Model):
    id = models.BigAutoField(primary_key=True)
    time = models.IntegerField()
    last_score = models.IntegerField()
    user = models.ForeignKey('Users', models.DO_NOTHING)
    capsule = models.ForeignKey(Capsules, models.DO_NOTHING)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scores'


class Sessions(models.Model):
    id = models.CharField(primary_key=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    user_id = models.BigIntegerField(blank=True, null=True)
    ip_address = models.CharField(max_length=45, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    user_agent = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    payload = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_activity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sessions'


class Shapes(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_shape = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    instrument_shape = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    tag = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    cause_shape = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    solution_shape = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    types_shape = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    information_shape = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    coordinates_shape = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    type_shape = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    color_shape = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    state_shape = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    technical_object = models.ForeignKey('TechnicalObjects', models.DO_NOTHING, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shapes'


class TechnicalObjectFile(models.Model):
    id = models.BigAutoField(primary_key=True)
    technical_object = models.ForeignKey('TechnicalObjects', models.DO_NOTHING)
    file = models.ForeignKey(Files, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'technical_object_file'


class TechnicalObjects(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    name_english = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    main = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    cover = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    gift = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description_1 = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description_2 = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    url_iteractivo = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    video = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    video_imagen = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    capacity = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    weight = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    length = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    width = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    height = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    requisition = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'technical_objects'


class Troubleshooting(models.Model):
    id = models.BigAutoField(primary_key=True)
    event = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    attributed_cause = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    superintendent = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    supervisor = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    operators = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    downtime = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    details = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    take_actions = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    results = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    equipment = models.ForeignKey(Equipments, models.DO_NOTHING)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'troubleshooting'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    surname = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    phone = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    email = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    system_type = models.IntegerField()
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    remember_token = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    sso = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Versions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_table = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    action = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    data = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    original_url = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    user = models.ForeignKey(Users, models.DO_NOTHING)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'versions'


class VirtualPlants(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    image = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    location = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    coordinates_plant = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    file = models.ForeignKey(Files, models.DO_NOTHING, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'virtual_plants'


class WebsocketsStatisticsEntries(models.Model):
    app_id = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    peak_connection_count = models.IntegerField()
    websocket_message_count = models.IntegerField()
    api_message_count = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'websockets_statistics_entries'
