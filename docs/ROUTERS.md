## GUIDELINES.md

##  Django REST Framework Routers: A Guide to Efficient API Development

Django REST Framework routers provide a powerful and elegant way to structure your API endpoints, minimizing code repetition and improving maintainability. This document will guide you through the best practices for using routers, along with practical examples.

**1. Understand the Basics**

* **Viewsets:** A viewset combines multiple views (e.g., list, detail, create, update, delete) into a single class. Routers interact directly with viewsets.
* **Routers:** Routers automatically generate URL patterns for your viewsets, reducing the need for manual URL configuration. DRF provides `SimpleRouter` and `DefaultRouter`.

**2. Choose the Right Router**

* **SimpleRouter:** Suitable for simple APIs with a limited number of endpoints. It registers viewsets at the root URL.
* **DefaultRouter:** Provides more features, such as automatic versioning and a prefix for registered viewsets.

**3. Register Viewsets**

* Use the `register()` method of the router to register your viewsets.
* Provide the URL prefix, the viewset class, and an optional `basename` for naming the URL patterns.
* Example:

```python
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, UserViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')
```

**4. Use Viewsets Effectively**

* **ModelViewSet:** Ideal for resources that support full CRUD operations (Create, Read, Update, Delete).
* **GenericViewSet:** More flexible, allowing you to customize which views are included.
* **Example (PostViewSet with ModelViewSet):**

```python
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

**5.  Handle Object-Level Permissions**

* Utilize the `has_object_permission` method within your viewset to implement granular permissions.
* **Example (IsAuthorOrReadOnly for PostViewSet):**

```python
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly 

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated, IsAuthorOrReadOnly)

    def has_object_permission(self, request, view, obj):
        # Allow read-only for all
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only allow write access for the author
        return obj.author == request.user
```

**6.  Create Additional Endpoints with Viewsets**

* Viewsets can have custom actions (e.g., `retrieve_by_category`). 
* Register custom actions using the `register()` method.
* **Example (Retrieve Posts by Category):**

```python
class PostViewSet(viewsets.ModelViewSet):
    # ... previous code ...

    @action(detail=False, methods=['get'])
    def retrieve_by_category(self, request, pk=None):
        category = request.query_params.get('category')
        posts = Post.objects.filter(category=category)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)
```

**7.  Real-world Application Examples**

* **Blog API:** 
    * Create a `PostViewSet` to handle the full CRUD operations for blog posts.
    * Utilize the `IsAuthorOrReadOnly` permission class to restrict editing and deleting to the post author.
* **E-commerce API:**
    * Create a `ProductViewSet` to handle products.
    * Implement additional viewset actions for features like filtering by category, adding products to a cart, or handling order creation.
* **Social Media API:** 
    * Create a `UserViewSet` to manage users.
    * Implement custom actions for following/unfollowing users, sending messages, or handling friend requests.

**8.  Key Advantages of Routers**

* **Reduced Code:** Minimal URL configuration and fewer views required.
* **Consistency:** Enforces a consistent structure for API endpoints.
* **Scalability:** Easily adaptable as your API grows more complex.
* **Maintainability:** Simplifies codebase navigation and updates.

**9.  Advanced Router Techniques**

* **Custom Routers:** Extend the `SimpleRouter` or `DefaultRouter` to add specific functionality.
* **Nested Routers:** Use nested routers to create hierarchical URL structures for related resources.

**Remember:**  Routers offer significant benefits in DRF development, but it's important to understand their purpose and use them effectively. Choose the right router, utilize viewsets appropriately, and implement custom actions as needed. This approach leads to a well-organized and maintainable API structure. 
