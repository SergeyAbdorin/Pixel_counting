from django.db import models


class ImageModel(models.Model):
    """
        All uploaded images from index page
    
        Attributes:
            image       -   ImageFiled

            upload_date -   dateField

    """

    image = models.ImageField(upload_to='images/', blank=False, null=False)
    upload_date = models.DateTimeField("upload date", auto_now_add=True)

    def __str__(self):
        return f'{self.image}'

    class Meta:
        db_table = 'Images'
        ordering = ['upload_date']


class PixelCount(models.Model):
    """
        Count pixels of all colors in the image from ImageModel

    Atributes:
        image           -   ImageModel object

        black_or_white  -   predominantly black or white

        hex_colors      -   all colors counts as JsonField
    """

    image = models.ForeignKey(
        ImageModel,
        on_delete=models.CASCADE,
        related_name='colors'
    )

    black_or_white = models.CharField(
        max_length=5,
        blank=False,
        null=False
    )

    hex_colors = models.JSONField(
        verbose_name="Colors",
        blank=False, null=False
    )

    class Meta:
        db_table = 'PixelCounts'
