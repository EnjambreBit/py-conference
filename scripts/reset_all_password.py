import sys
import os
import django

sys.path.append("..")
sys.path.append(".")

# Configuración inicial de django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from django.contrib.auth.models import User

password = "asdasd123"

print("")
print("Reiniciando contraseñas de: \n")

for user in User.objects.order_by("username"):
    user.set_password(password)

    if user.is_superuser:
        print(" - Usuario Administrador:", user)
    else:
        print(" - Usuario", user)

    user.save()

print("")