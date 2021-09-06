# User authentication in Django Normal Vs. Ajax
# Demo Normal Django Authentication

Overview¶
The Django authentication system handles both authentication and authorization.
Briefly, authentication verifies a user is who they claim to be, and authorization
determines what an authenticated user is allowed to do. Here the term authentication
is used to refer to both tasks.
## The auth system consists of:
* Users
* Permissions: Binary (yes/no) flags designating whether a user may perform a certain task.
* Groups: A generic way of applying labels and permissions to more than one user.
* A configurable password hashing system
* Forms and view tools for logging in users, or restricting content
* A pluggable backend system
<br>
The authentication system in Django aims to be very generic and doesn’t provide some features commonly found in web authentication systems. Solutions for some of these common problems have been implemented in third-party packages:

* Password strength checking
* Throttling of login attempts
* Authentication against third-parties (OAuth, for example)
* Object-level permissions
