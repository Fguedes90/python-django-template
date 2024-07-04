## GUIDELINES.md

## Django REST Framework Validations: A Guide to Data Integrity

Django REST Framework (DRF) provides powerful validation mechanisms to ensure that data submitted to your API meets specific criteria. This document will guide you through best practices and examples for implementing effective validation.

**1. Built-in Validators**

* **Field-Level Validation:** DRF provides several built-in validators that you can apply directly to serializer fields.
    * **`required=True`:**  Ensures that a field is not empty.
    * **`max_length=100`:**  Limits the maximum length of a string field.
    * **`min_value=10`:**  Sets a minimum value for numerical fields.
    * **`email`:** Validates that a field conforms to email format.
    * **`URL`:** Validates that a field conforms to URL format.
* **Example (Blog API):**

```python
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200, required=True)
    body = serializers.CharField()
    author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'created_at')
```

**2.  Custom Validators**

* **`validators` Attribute:**  Add custom validators to a field using the `validators` attribute.
* **Custom Validator Functions:**  Create your own validator functions that take a single argument (the field value) and raise a `ValidationError` if the validation fails.
* **Example (Product API):**

```python
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, required=True, validators=[
        UniqueValidator(queryset=Product.objects.all(), message="Product name must be unique.")
    ])
    # ... rest of the serializer ...
```

**3.  Model Validation**

* **`clean_*()` Methods:**  You can leverage Django's model validation by creating `clean_*()` methods on your models. These methods will be called during serializer validation.
* **Example (Blog API):**

```python
from django.core.exceptions import ValidationError

class Post(models.Model):
    # ... model fields ...

    def clean(self):
        if self.title == self.body:
            raise ValidationError("Title and body cannot be the same.")
        return super().clean()
```

**4.  Validation at Different Levels**

* **Field-Level:**  Validate individual fields using built-in or custom validators.
* **Object-Level:**  Validate the entire serialized data using the `validate()` method.
* **Example (Order API):**

```python
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    # ... fields and validation ...

    def validate(self, attrs):
        # Check if the total cost is valid
        total_cost = attrs.get('total_cost')
        if total_cost < 10:
            raise serializers.ValidationError("Total cost must be at least 10.")
        return attrs
```

**5. Real-world Application Examples**

* **E-commerce API:**
    * **Product Serializer:**  Validate product name uniqueness, price range, and category selection.
    * **Order Serializer:** Validate total cost, ensure sufficient inventory for ordered products, and check for valid shipping address.
* **Social Media API:**
    * **User Serializer:**  Validate username uniqueness and email format.
    * **Post Serializer:**  Validate post content length, image dimensions (if applicable), and ensure the user has the permission to post.
* **Task Management API:**
    * **Task Serializer:** Validate task title, due date range, and assign the task to an existing user.

**6.  Key Advantages of Validation**

* **Data Integrity:** Ensures that data submitted to your API is consistent and meets your application's requirements.
* **Error Handling:** Provides informative error messages to clients when validation fails, making it easier to identify and correct issues.
* **Security:** Protects against malicious data injection and other security threats.
* **Maintainability:**  Encapsulates validation logic within serializers, keeping your API logic clean and organized.
* **Testability:**  Easily write unit tests for your serializers and validation rules, making it easier to ensure data integrity.

**7.  Remember:**

* **Use Built-in Validators Where Possible:**  Leverage DRF's built-in validators for common validation tasks.
* **Create Custom Validators for Specific Needs:**  Write custom validators to enforce unique rules or complex validation logic.
* **Prioritize Model Validation:** Use `clean_*()` methods for validation logic related to model constraints.
* **Validate at Multiple Levels:**  Use field-level, object-level, or model-level validation to ensure data integrity.
* **Provide Clear Error Messages:**  Write informative error messages for clients to help them correct issues.
* **Test Thoroughly:**  Write unit tests to verify that your validation rules are working as expected.

By effectively implementing validation in your DRF serializers, you can build robust and reliable APIs that handle data with confidence and protect your application from vulnerabilities.


