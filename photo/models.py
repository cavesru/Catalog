from django.db import models
from django.utils import timezone

from album.models import Album

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class Photo(models.Model):
    owner = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    photo = models.ImageField(upload_to='images/%Y/%m/%d')
    thumb = models.ImageField(upload_to='thumbs/%Y/%m/%d', blank = True, null = True)
    
    album = models.ForeignKey(Album, related_name='photo')
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def thumb_make(self):
        max_width = 242
        max_height = 200
            
        thumb = Image.open(self.photo)

        src_width, src_height = thumb.size
        src_ratio = float(src_width) / float(src_height)
        dst_width, dst_height = max_width, max_height
        dst_ratio = float(dst_width) / float(dst_height)
        
        if dst_ratio < src_ratio:
            crop_height = src_height
            crop_width = crop_height * dst_ratio
            x_offset = float(src_width - crop_width) / 2
            y_offset = 0
        else:
            crop_width = src_width
            crop_height = crop_width / dst_ratio
            x_offset = 0
            y_offset = float(src_height - crop_height) / 3
                
        thumb = thumb.crop((int(x_offset), int(y_offset), int(x_offset+crop_width), int(y_offset+crop_height)))
        thumb = thumb.resize((dst_width, dst_height), Image.ANTIALIAS)
            
        thumb_io = BytesIO()
        thumb.save(thumb_io, format='JPEG')
        thumb_file = InMemoryUploadedFile(thumb_io, None, str(self.photo), 'image/jpg', len(thumb_io.getvalue()), None)

        self.thumb.save (str(thumb_file), thumb_file, save=True)