from django.core.management.base import BaseCommand
from myapp.models import MyModel, transaction, threading

class Command(BaseCommand):
    help = 'Create a MyModel instance and trigger signal'

    def handle(self, *args, **kwargs):
        self.create_model_instance()

    def create_model_instance(self):
        print(f"Saving model instance in thread: {threading.current_thread().name}")
        
        # Question 3: Prove same transaction
        with transaction.atomic():
            instance = MyModel(name="Test")
            instance.save()
            print(f"Transaction state in save (autocommit): {transaction.get_autocommit()}")
            print("Model instance saved")
            # Simulate error to prove the transaction rollback, if desired:
            # raise Exception("Error occurred, triggering rollback")
