from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, mobile_no, password=None, **extra_fields):
        if not mobile_no:
            raise ValueError('Mobile no. is required!')

        user = self.model(mobile_no=mobile_no, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, mobile_no, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(mobile_no, password, **extra_fields)
