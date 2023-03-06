from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class CountryData(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	country = models.CharField(max_length=100, default='NewCountry')
	population = models.IntegerField()
	money = models.IntegerField()
	dateNow = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'Country Population Data'

	def __str__(self):
		return f'{self.country}-{self.population}'

class ProfileModel(models.Model):
	# One user from django admin is equal to one profile (One to one)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to='profile', default='avatar.jpg', validators=[
		FileExtensionValidator(['png', 'jpg'])])

	def __str__(self):
		return f'{self.user.username}'