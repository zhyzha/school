from django.db import models

GENDER_FEMALE = 'F'
GENDER_MALE = 'M'

GENDER_CHOICES = (
    (GENDER_FEMALE, 'Female'),
    (GENDER_MALE, 'Male'),
)
class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True)
    email = models.EmailField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=12)

    class Meta:
        ordering = ['-first_name']
        unique_together = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
        )


    def save(self, *args, **kwargs):
        for field_name in ['first_name', 'last_name']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Student, self).save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     self.first_name = self.first_name.capitalize()
    #     self.last_name = self.last_name.capitalize()
    #     super(Student, self).save()
        #vtotoi sposob, no medlennee chem pervyi

    def __str__(self):
        return self.first_name



