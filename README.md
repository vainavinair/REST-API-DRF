
# Django REST Framework Product API

This is a Django REST Framework (DRF) API that allows you to manage products. It provides endpoints for creating, retrieving, updating, and deleting products.

## Prerequisites

Before running the API, make sure you have the following installed:

- Python (version 3.7 or higher)
- Django (version 4.2.1)
- Django REST Framework (version 3.12 or higher)
- PostgreSQL database

## Installation

1. Clone the repository:

   ```shell
   $ git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```shell
   $ cd <project-directory>
   ```

3. Install the required dependencies:

   ```shell
   $ pip install -r requirements.txt
   ```

4. Database Configuration:
   
   Update the database configuration in the `settings.py` file located in the `ecom_api` directory. Set the correct values for the following properties under the `DATABASES` dictionary:

   - `'NAME'`: The name of your PostgreSQL database.
   - `'USER'`: The username to access the database.
   - `'PASSWORD'`: The password to access the database.

5. Run the database migrations:

   ```shell
   $ python manage.py migrate
   ```

6. Start the development server:

   ```shell
   $ python manage.py runserver
   ```

   The API will be accessible at `http://localhost:8000/`.

## API Endpoints

The following endpoints are available in the API:

- `GET api/home/`: Get a list of all products.
- `GET api/{id}/detail/`: Get details of a specific product.
- `POST api/create/`: Create a new product.
- `POST api/create/many/`: Create multiple products in a single request.
- `PUT api/{id}/update/`: Update an existing product.
- `DELETE api/{id}/delete/`: Delete an existing product.

## Authentication and Permissions

The API uses token-based authentication to secure the endpoints. To access the protected endpoints, you need to obtain an access token by providing your credentials (username and password) to the `/token/` endpoint. Include the access token in the `Authorization` header of subsequent requests as follows: `Authorization: Bearer <access-token>`, where `<access-token>` is the token obtained.

The API provides the following authentication endpoints using the `Simple JWT` library:

`POST user/token/`: Obtain an access token by providing your credentials. This endpoint validates the provided username and password, and if they are correct, it returns an access token and a refresh token in the response.
`POST user/token/refresh/`: Refresh an access token using a valid refresh token. This endpoint allows you to obtain a new access token without having to provide your credentials again. You need to include a valid refresh token in the request, and if it is valid, a new access token is returned.

The API also includes the following permissions:
- `IsAuthenticated`: Only authenticated users can access the endpoints.
- `IsOwner`: Only the owner of a product can update or delete it.

## Filtering, Ordering, and Searching

The API supports filtering, ordering, and searching on the `api/home/` endpoint. You can use the following query parameters:

- `category`: Filter products by category.
- `user`: Filter products by the username of the owner.
- `ordering`: Order products by price (ascending or descending).
- `search`: Search products by name, description, category, or username.

Example usage:

- `GET api/home/?category=electronics`: Get all products in the electronics category.
- `GET api/home/?user=johndoe`: Get all products owned by the user with the username "johndoe".
- `GET api/home/?ordering=price`: Order products by price in ascending order.
- `GET api/home/?search=phone`: Search for products with the keyword "phone" in their name, description, category, or owner's username.

## Screenshots
### List View/Read
![List View](screenshots\home_endpoint.png)
### Detail View
![Detail View](screenshots\detail_endpoint.png)
### Sorted View
![Sorting](screenshots\sort.png)
### Filter,Search
![Filter,Search](screenshots\filter.png)
### Create 
![Create](screenshots\create_endpoint.png)
### Permission Check
![Permission](screenshots\permission.png)
### Update 
![Update](screenshots\update_endpoint.png)
### Delete 
![Delete](screenshots\delete_endpoint.png)
### Token 
![Token](screenshots\token_endpoint.png)


