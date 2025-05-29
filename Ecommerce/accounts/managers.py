from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    
    def create_user(self, phone, email, name, password=None):

        if not phone:
            raise ValueError('Users must have phone number')
        if not email:
            raise ValueError('Users must have email address')
        if not name:
            raise ValueError('Users must have full name')
        
        user = self.model(
            phone = phone,
            email = self.normalize_email(email),
            name = name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, phone, email, name, password=None):
        user = self.create_user(phone, email, name, password)
        user.is_admin = True
        user.save(using=self._db)
        return user
    