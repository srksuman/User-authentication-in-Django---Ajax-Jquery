# User Authentication In Django/Ajax/Jquery
# Demo: Authentication System Using Django/Ajax/Jquery
![ajax](https://user-images.githubusercontent.com/67781881/132255146-7ec7ec6d-307d-4e14-b4a9-3ba8813c8b1d.gif)
# Demo: Authentication System Using Django
![normal](https://user-images.githubusercontent.com/67781881/132255095-4123af41-ee2f-4fa6-bf35-ac3dd171e516.gif)

Overview
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
