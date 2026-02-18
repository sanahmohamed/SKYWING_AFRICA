from django.db import models


class Registration(models.Model):
    BUDGET_CHOICES = [
        ('300K-1M', '300K - 1M'),
        ('1M-3M', '1M - 3M'),
        ('2.5M-5M', '2.5M - 5M'),
    ]

    TYPE_CHOICES = [
        ('TOWNHOUSE', 'Townhouse'),
        ('VILLA', 'Villa'),
        ('APPARTMENT', 'Appartment'),
    ]

    DATE_CHOICES = [
        ('2026-03-21', '2026-03-21'),
        ('2026-03-22', '2026-03-22'),
        
    ]

    TIMESLOT_CHOICES = [
        ('9:00-12:00', '9:00 TO 12:00'),
        ('12:00-15:00', '12:00 TO 15:00'),
        ('15:00-18:00', '15:00 TO 18:00'),
        ('18:00-21:00', '18:00 TO 21:00'),
    ]

    #Full Name
    full_name = models.CharField(max_length=200, verbose_name='Full Name')

    #Contact Number
    contact_number = models.CharField(max_length=50, verbose_name='Contact Number)')

    # Email
    email = models.EmailField(verbose_name='Email Address')

    # Nationality
    nationality = models.CharField(max_length=100, verbose_name='Nationality')

    age = models.IntegerField(verbose_name='Age', null=True, blank=True)

    #Budget
    budget = models.CharField(
        max_length=20,
        choices=BUDGET_CHOICES,
        default='300K-1M',
        verbose_name='Budget'
    )

    # 06 房型 - Property Type
    property_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default='TOWNHOUSE',
        verbose_name='Property Type'
    )

    #  Date of Attending
    date_of_attending = models.CharField(
        max_length=20,
        choices=DATE_CHOICES,
        default='2026-03-21',
        verbose_name='Date of Attending'
    )

    #  Time Slot
    time_slot = models.CharField(
        max_length=20,
        choices=TIMESLOT_CHOICES,
        default='9:00-12:00',
        verbose_name='Time Slot'
    )

    #  Reference
    reference = models.TextField(
        blank=True,
        null=True,
        verbose_name='Reference'
    )

    # Metadata
    submitted_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)

    class Meta:
        verbose_name = 'Registration'
        verbose_name_plural = 'Registrations'
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.full_name} - {self.date_of_attending} ({self.time_slot})"
