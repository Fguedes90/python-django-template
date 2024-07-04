## AUTH.md

## Authentication and Authorization in Django REST Framework: JWT and Permissions

This document will guide you through the implementation of authentication and authorization in Django REST Framework (DRF) using JSON Web Tokens (JWT) and permissions.

**1. Authentication: Verifying User Identity**

* **Authentication:** The process of verifying a user's identity and granting access to protected resources. DRF provides several authentication mechanisms, including:
    * **Session Authentication:** Uses Django's built-in session system and cookies.
    * **Basic Authentication:**  Sends credentials (username/password) as a base64 encoded string in the HTTP header.
    * **Token Authentication:**  Uses JWTs to securely identify users.
    * **OAuth2 Authentication:**  Utilizes third-party services for user authentication.

* **JWT (JSON Web Token):**  A standard for securely transmitting information between parties as a JSON object.
    * **Components:**
        * **Header:**  Contains the token type and algorithm used.
        * **Payload:**  Contains user-specific data (e.g., ID, username).
        * **Signature:**  Ensures the token's integrity and authenticity.
    * **Advantages:**
        * **Stateless:**  No session management required on the server.
        * **Scalability:** Easily handles a large number of users.
        * **Secure:**  Utilizes cryptographic signing for verification.

**2.  Implementing JWT Authentication**

* **Install `djangorestframework-simplejwt`:**  
   ```bash
   pip install djangorestframework-simplejwt
   ```

* **Add to `INSTALLED_APPS`:**
    ```python
    INSTALLED_APPS = [
        # ... other apps ...
        'rest_framework',
        'rest_framework.authtoken',
        'rest_framework_simplejwt',  # Add this
        'rest_framework_simplejwt.token_blacklist',  # Optional for token blacklisting
        # ... other apps ...
    ]
    ```

* **Configure Authentication Settings:**
    ```python
    REST_FRAMEWORK = {
        # ... other settings ...
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        ]
    }
    ```

* **Create JWT Token Views:**
    ```python
    from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )

    urlpatterns = [
        path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]
    ```

* **Example (Login Endpoint):**

    ```python
    from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
    from rest_framework.decorators import api_view
    from rest_framework.response import Response

    @api_view(['POST'])
    def login(request):
        serializer = TokenObtainPairSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    ```

**3.  Authorization: Controlling Access**

* **Authorization:**  The process of determining which actions a user is allowed to perform on specific resources. 
* **Permissions:** DRF provides a mechanism for managing authorization using permissions classes.
    * **`AllowAny`:** Grants access to all users (authenticated or not).
    * **`IsAuthenticated`:** Grants access only to authenticated users.
    * **`IsAdminUser`:** Grants access only to users with administrative privileges.

**4.  Implementing Permissions**

* **View-Level Permissions:**  Apply permissions to individual views.
* **Object-Level Permissions:** Apply permissions to specific objects based on conditions.
* **Custom Permissions:**  Create your own custom permission classes to implement specific authorization logic.

**5.  Example:  Restricting Blog Post Editing to Authors**

```python
from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner of the snippet.
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    # ... other code ...
    permission_classes = (permissions.IsAuthenticated, IsAuthorOrReadOnly)
```

**6.  Example:  Admin-Only Permissions**

```python
class AdminOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff

class UserViewSet(viewsets.ModelViewSet):
    # ... other code ...
    permission_classes = (permissions.IsAuthenticated, AdminOnly) 
```

**7.  Integrating JWT and Permissions**

* When using JWT authentication, your API views will automatically be protected by the `IsAuthenticated` permission.
* You can add additional permissions classes to your views for more granular authorization control.

**8.  Remember:**

* Use `djangorestframework-simplejwt` for robust JWT authentication.
* Create custom permissions classes for specific authorization needs.
* Securely store your JWT secret key and other sensitive configurations.
* Use JWT tokens for stateless authentication and a more scalable API.

By implementing JWT authentication and proper permissions, you can ensure that only authorized users have access to your API resources, enhancing security and maintaining data integrity. 

