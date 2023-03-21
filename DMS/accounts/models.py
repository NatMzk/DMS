from django.db import migrations, models


# Class that represent table model from PostgreSQL database
class device_power_consumption(models.Model):
	device_id = models.IntegerField()
	datestmp = models.TextField()
	timestmp = models.TextField()
	global_active_power = models.TextField()
	global_reactive_power = models.TextField()
	voltage = models.TextField()
	global_intensity = models.TextField()
	sub_metering_1 = models.TextField()
	sub_metering_2 = models.TextField()
	sub_metering_3 = models.TextField()

	class Meta:
		db_table = "device_power_consumption" # Name of the PostgreSQL table that data is pulled from



class device_dim(models.Model):
	device_id = models.IntegerField()
	device_name = models.TextField()
	device_model = models.TextField()
	device_status = models.TextField()

	class Meta:
		db_table = "device_dim" # Name of the PostgreSQL table that data is pulled from


