from django.db import models

user = 'kiruha'


class LaunchData(models.Model):
    launch_time = models.DateTimeField()
    rocket_name = models.CharField(max_length=20, default="Wasley Rocket")
    launch_coordinates = models.CharField(max_length=100)
    launch_img = models.ImageField(upload_to=f'{user}/%Y/%m/%d/', height_field='height', width_field='width')
    width = models.IntegerField(editable=False)
    height = models.IntegerField(editable=False)
    launch_description = models.TextField()

    def __str__(self):
        return str(self.launch_time)


class CommonData(models.Model):
    whose_param = models.CharField(max_length=20, default="Atmosphere")
    measure = models.CharField(max_length=20)
    value = models.FloatField()
    measure_time = models.DateTimeField()
    dimension = models.CharField(max_length=5)
    launch_id = models.ForeignKey(to=LaunchData, on_delete=models.CASCADE)

    def __str__(self):
        return self.measure
