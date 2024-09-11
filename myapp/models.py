import threading
import time
from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    # Question 1: Prove synchronous execution
    print(f"Signal handler started in thread: {threading.current_thread().name}")
    time.sleep(3)  # Simulate some time-consuming task
    print(f"Signal handler finished in thread: {threading.current_thread().name}")
    
    # Question 3: Prove same transaction
    print(f"Transaction state inside handler (autocommit): {transaction.get_autocommit()}")

