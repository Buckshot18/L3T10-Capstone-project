from django.db import models
from django.contrib.auth.models import User

class BandMember(models.Model):
    """
    Model representing a band member in the music band.

    Attributes:
        name (str): The name of the band member.
        instrument (str): The instrument the band member plays.
        bio (str): A short biography of the band member.

    Methods:
        __str__(self): Returns the name of the band member as a string representation.
    """

    # The name of the band member. This is a required field with a max length of 100 characters.
    name = models.CharField(max_length=100)

    # The instrument that the band member plays. This is also a required field with a max length of 100 characters.
    instrument = models.CharField(max_length=100)

    # A short biography or description of the band member. This field can store larger amounts of text.
    bio = models.TextField()

    def __str__(self):
        """
        String representation of the BandMember object.

        Returns:
            str: The name of the band member
        """
        return self.name

class Event(models.Model):
    """
    Model representing an event (e.g., a concert or performance) where the band performs.

    Attributes:
        title (str): The title or name of the event.
        date (date): The date of the event.
        location (str): The location where the event will take place.

    Methods:
        __str__(self): Returns the title of the event as a string representation.
    """

    # The title or name of the event, such as "Summer Concert" or "Album Release Party."
    title = models.CharField(max_length=200)

    # The date when the event will take place. This is a required field for all events.
    date = models.DateField()

    # The location of the event (venue, city, etc.), with a maximum length of 200 characters.
    location = models.CharField(max_length=200)

    def __str__(self):
        """
        String representation of the Event object.

        Returns:
            str: The title of the event.
        """
        return self.title
