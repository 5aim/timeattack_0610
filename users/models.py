from django.db import models

class User(models.Model): # 모델을 상속해야 데이터베이스에 접근하거나 Query할 수 있다.
    email = models.EmailField(max_length=100, null=False, unique=True)
    password = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users' # table 이름 users
        