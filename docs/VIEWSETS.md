## GUIDELINES.md

##  Django REST Framework Viewsets: A Guide to Efficient API Development

Django REST Framework (DRF) viewsets provide a powerful and elegant way to structure your API endpoints, minimizing code repetition and improving maintainability. This document will guide you through the best practices for using viewsets, along with practical examples.

**1. Understand the Basics**

* **Viewsets:** A viewset combines multiple views (e.g., list, detail, create, update, delete) into a single class. This allows for more organized and reusable code.
* **Generic Views:** DRF provides generic views like `ListAPIView`, `RetrieveAPIView`, `CreateAPIView`, `UpdateAPIView`, `DestroyAPIView`, and `RetrieveUpdateDestroyAPIView` for common API actions.
* **ModelViewSet:** DRF's `ModelViewSet` is a powerful viewset that includes all CRUD (Create, Read, Update, Delete) operations for a given model.

**2. Choosing the Right Viewset**

* **ModelViewSet:** Ideal for resources that support full CRUD operations. It's often the simplest and most convenient option.
* **GenericViewSet:** More flexible and allows for greater customization. Use it when you need to control the specific views included in your viewset.
* **Custom Viewset:** Create your own viewset class for highly specialized API endpoints or complex logic.

**3. ModelViewSet Example: Blog API**

```python
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated, IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
```

**4.  GenericViewSet Example: User API (Partial CRUD)**

```python
from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

class UserViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
```

**5.  Customizing Views with Actions**

*  Add custom actions to your viewset using the `@action` decorator.
*  Specify the action's URL pattern, methods, and details.
* **Example: Get Posts by Category**

```python
from rest_framework.decorators import action
from rest_framework.response import Response

class PostViewSet(viewsets.ModelViewSet):
    # ... previous code ...

    @action(detail=False, methods=['get'])
    def retrieve_by_category(self, request, pk=None):
        category = request.query_params.get('category')
        posts = Post.objects.filter(category=category)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)
```

**6. Real-world Application Examples**

* **E-commerce API:**
    * Create a `ProductViewSet` using `ModelViewSet` to handle products, including CRUD operations.
    * Add custom actions for product filtering (by category, price, etc.) or adding products to a cart.
* **Social Media API:** 
    * Create a `UserViewSet` using `GenericViewSet` and mixins for user listing, retrieval, and updating.
    * Implement actions for following/unfollowing users, sending messages, or handling friend requests.
* **Task Management API:**
    * Create a `TaskViewSet` using `ModelViewSet` to handle tasks with CRUD operations.
    * Add actions for task assignment, priority updates, and completion marking.

**7.  Key Advantages of Viewsets**

* **Code Reusability:**  Reduce redundant code by combining multiple related views into one viewset.
* **Organization:**  Improve code structure and maintainability by grouping related API logic.
* **Flexibility:**  Easily add custom actions or modify existing behavior using mixins.
* **Scalability:** Adaptable as your API grows more complex, providing a structured and consistent foundation.

**8.  Advanced Viewset Techniques**

* **Permissions:**  Implement object-level permissions for specific actions within your viewset.
* **Serialization:** Utilize different serializers for different actions (e.g., a serializer for creating a post and another for updating it).
* **Custom Logic:**  Override methods like `create()`, `update()`, or `destroy()` to add custom logic for your API actions.

**9.  Remember:**

* Start with `ModelViewSet` when possible, but don't hesitate to use `GenericViewSet` or custom viewsets if you need more flexibility.
* Carefully consider the appropriate permissions for each action within your viewset.
* Write thorough unit tests for your viewsets to ensure their correct functionality.
* Keep your viewsets concise and focused on a specific resource.
* Use routers in conjunction with viewsets to automate URL pattern generation for a streamlined API structure.

By leveraging viewsets, you can create well-organized, maintainable, and scalable Django REST Framework APIs, focusing on core functionality and simplifying development.
