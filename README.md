# timeattack_0610

스파르타 코딩클럽 내일배움캠프 AI 2기

---

1. Django 프로젝트를 생성하고, user, product 라는 앱을 만들어서 settings.py에 등록

---

## models

2. user/models models.py : <email, password>를 받을수 있는 `User` 이라는 모델을 만들어보세요. (인증은 별도로 구현하지 않을 예정이므로 최대한 간단하게!) 

3. product/models models.py : <상품 이름, 상품 카테고리, 이미지, 설명, 가격, 재고량>이 들어갈 수 있는 `Product` 이라는 모델을 만들어보세요.

4. product/models.py :<상품의 카테고리 이름>이 들어갈 수 있는 `Category` 라는 모델을 만들어보세요.

5. product/models.py : 주문한 상태(주문 완료, 결제 완료, 취소, 배송출발, 배송완료) 을 저장할 수 있는 `OrderStatus`라는 모델을 만들어보세요.

6. 카테고리에 따른 상품만 나타나도록 `Category`와 `Product`간의 관계를 설정해보세요. (힌트: one-to-many 또는 many-to-many 관계 이용)

7. 유저가 주문한 상품의 개수를 저장하는 `ProductOrder` 하는 모델을 만들어 보세요.

8. product/models.py : 유저의 주문(배송주소, 주문시간, 전체 상품 가격, 할인율, 최종가격, 유효여부(boolean) )을 저장할 수 있는 `UserOrder`라는 모델을 만들어보세요.

9. 유저가 상품을 주문할 수 있고 주문 상태를 관리하도록 위에서 만든 User, Category, Product, OrderStatus, UserOrder, ProductOrder 테이블들의 관계를 맺어보세요. 

(모델링은 요구사항에 따라 효율적인 방식이 다르므로 요구사항만 충족하도록 관계 설정하거나 테이블을 만들어도됨)

10. 모델을 작성하고 migrations/migrate 이후 Admin 페이지를 통해서, `Category` 모델에 `laptop`, `mobile`라는 카테고리를 각각 생성해보세요.

11. Admin 페이지 또는 다른 방법을 통해서 각 `Category`에 해당하는 상품을 두개씩 넣어보세요.

12. Admin 페이지 또는 다른 방법을 통해서 각 `OrderStatus`에 주문 완료(order placed), 결제완료(paid), 배송완료(completed), 발송완료(sent), canceled 상태를 넣어보세요

13. 테스트를 위해서 python manange.py shell 을 이용하여 User 모델을 2개정도 생성해서 테스트

---

## view / template

14. product/views.py : get 메소드에서 선택하는 카테고리에 따라 상품리스트 보여주는 view와 템플릿을 구현해보세요.

15. product/views.py : 주문 하기 버튼을 선택했을 때 주문페이지로 이동할수 있도록 view와 템플릿을 구현해보세요.

16. poduct/views.py : post 메소드에서 `상품명`, `개수`, `주소를` 받아서 위에서 작성한 ProductOrder, UserOrder을 create 하는 주문 메소드를 구현해보세요. ( OrderStatus 주문한 상태이므로 order placed 를 가져와서 만들것!)

- 유저 정보는 id =1  또는 생성한 유저로 하드코딩 할것!


---

# 참고자료

## models

### 1. django squash migrations

- squash : 짓누르다, 으깨다, 찌부러뜨리다, (좁은 곳에) 밀어 넣다 [쑤셔 박다]

https://docs.djangoproject.com/en/4.1/topics/migrations/#squashing-migrations

### 2. ImageField 사용예제

https://docs.djangoproject.com/en/4.0/topics/files/

### 3. shell

  - python manage.py shell
  - shell을 써서 User model 생성해보기
  - window의 경우 import 해줘야 함.

```shell
from users.models import User

User

dir(User)

import inspect

for i in inspect.getmembers(User):
    print(i)
    
User.objects.create(email='lee', password='1234')

User.objects.create(email='kim', password='4321')

user = User.objects.get(id=1)

user.email

user.password

user.created_at
```

## view / templates

### 1. GET